# 下载 http://gss0.baidu.com/7Po3dSag_xI4khGko9WTAnF6hhy/zhidao/pic/item/2e2eb9389b504fc26a5a3b12eddde71190ef6da4.jpg 这张图片到桌面 命名为大白.png

import requests
import os

url='http://gss0.baidu.com/7Po3dSag_xI4khGko9WTAnF6hhy/zhidao/pic/item/2e2eb9389b504fc26a5a3b12eddde71190ef6da4.jpg'
deskPath="C:\\Users\\Administrator\\Desktop\\test\\"

if not os.path.exists(deskPath):
    os.makedirs(deskPath)
req=requests.get(url)
if req.status_code==200:
    f=open(deskPath+"大白.png","wb+")
    f.write(req.content)
    f.close()
else:
    print("下载错误错误")

