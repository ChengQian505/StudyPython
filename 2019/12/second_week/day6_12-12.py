# 在桌面新建test文件夹
# 文件夹内创建一个1.txt 内容为 我当前创建了一个文件
# 文件夹内创建一个2.txt 内容是 1.txt的内容再追加 \n但是我是copy的

import os

deskPath="C:\\Users\\Administrator\\Desktop\\test\\"

# task1

if not os.path.exists(deskPath):
    os.makedirs(deskPath)

# task2

f_w=open(deskPath+"1.txt","w+")
f_w.write("我当前创建了一个文件")
f_w.close()

# task3
f_r=open(deskPath+"1.txt","r")
f2=open(deskPath+"2.txt","w+")
f2.write(f_r.read()+"\n但是我的copy的")
f_r.close()
f2.close()
