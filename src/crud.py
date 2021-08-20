from database import UserToQQ

from sqlalchemy.orm import Session


def add_user(db: Session, wx_id: str, qq: str) -> UserToQQ:
    user_to_qq = UserToQQ(
        wx_id=wx_id,
        qq=qq
    )
    db.add(user_to_qq)
    db.commit()
    db.flush()
    return user_to_qq


def get_qq_by_wx(db: Session, wx_id: str) -> str:
    item = db.query(UserToQQ).filter(UserToQQ.wx_id == wx_id).first()
    if item:
        return item.qq
