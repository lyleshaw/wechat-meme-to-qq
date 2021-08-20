# wechat-meme-to-qq [![Python 3.7](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/release/python-379/)

A Kit That Can Convert WeChat Meme to QQ

## Cause

虽然目前相当一部分人都全盘转向了微信，但是仍有一些人只能在QQ上找到。

这时，我和一部分朋友（在同时使用QQ和微信时）遇到一个有点难受的问题，即二者的表情包是不同步的...并且仅仅QQ的表情包可以传到微信，微信的表情包却很难导出。

于是，在鸽了许久之后，我终于动手并花了一个晚上完成这个项目...

简而言之，在微信端绑定了QQ号后，对该微信发的所有表情包将会一键转移到QQ上！

（虽然有点蠢但是大概或许稍微还是有点用叭...）

## Usage

> 私有化部署需拥有一个 Wechaty Token 哦！
> 同时需搭建一个 cqhttp 的 QQ 机器人。

```shell
python3 src/main.py
```

## Example

同时添加如下两个微信/QQ。

![image](https://user-images.githubusercontent.com/25427168/130254178-b7c33cfe-135e-4c73-951e-9c40e5bc383f.png)
![image](https://user-images.githubusercontent.com/25427168/130254207-fe85c17b-11ff-420f-8d1a-8fe5823cbede.png)

然后就可以使用啦！

![image](https://user-images.githubusercontent.com/25427168/130254457-33eff23b-6e2e-416e-af48-0554fc725a84.png)

## Authors

- [@Lyle](https://github.com/lyleshaw) - Lyle Shaw (肖良玉)

## Copyright & License

* Code & Docs © 2020-now Lyle Shaw \<x@lyleshaw.com\>
* Code released under the Apache-2.0 License
* Docs released under Creative Commons
