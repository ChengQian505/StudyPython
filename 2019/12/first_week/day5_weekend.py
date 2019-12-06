# 打印九九乘法表

for i in range(1,10):
    for j in range(1,i+1):
        result=i*j
        if result<10:
            result=str(result)+" "
        else:
            result=str(result)
        if j == i:
            print(str(i)+"*"+str(j)+'='+result)
        else:
            print(str(i) + "*" + str(j) + '=' + result, end=' ')
