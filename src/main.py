import re
import base64
import asyncio
import logging
from typing import Optional, Union

import requests
import wechaty
from wechaty import (
    FileBox,
    Wechaty,
    Contact,
    Room,
    Message
)

from config import CQ_API_URL
from crud import get_qq_by_wx, add_user
from database import Base, engine, Session, SessionLocal

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class MemeBot(Wechaty):
    
    def __init__(self):
        self.login_user: Optional[Contact] = None
        super().__init__()
    
    @staticmethod
    def check_qq(self, text: str) -> [bool, str]:
        pattern = re.compile("[1-9]\\d{4,10}")
        if len(pattern.findall(text)) == 1:
            return True, pattern.findall(text)[0]
        return False, ''
    
    async def on_message(self, msg: Message):
        from_contact: Contact = msg.talker()
        text: str = msg.text()
        room: Optional[Room] = msg.room()
        file_box = None
        if msg.type() in wechaty.user.message.SUPPORTED_MESSAGE_FILE_TYPES:
            file_box: Optional[FileBox] = await msg.to_file_box()
        db: Session = SessionLocal()
        conversation: Union[Room, Contact] = from_contact if room is None else room
        await conversation.ready()
        
        qq = get_qq_by_wx(db=db, wx_id=conversation.contact_id)
        is_qq, checked_qq = self.check_qq(self=self, text=text)
        if file_box and qq:
            str_img = base64.b64encode(requests.get(file_box.remoteUrl).content).decode("utf-8").replace("b'", "").replace("'", "")
            requests.post(
                url=f'{CQ_API_URL}/send_msg',
                json={
                    'user_id': qq,
                    'message': f'[CQ:image,file=base64://{str_img}, type=show,id=40000]'
                }
            )
        elif is_qq:
            add_user(db=db, wx_id=conversation.contact_id, qq=checked_qq)
            await conversation.say('绑定成功！')
        elif not qq:
            await conversation.say('请输入QQ号以完成绑定！')
        db.close()
    
    async def on_login(self, contact: Contact):
        logger.info('Contact<%s> has logined ...', contact)
        self.login_user = contact


bot: Optional[MemeBot] = None


async def main():
    Base.metadata.create_all(bind=engine)
    global bot
    bot = MemeBot()
    await bot.start()


asyncio.run(main())
