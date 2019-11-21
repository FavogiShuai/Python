
try:
    f = open('./test.txt')
    # 逐行读取
    # while True:
    #     s = f.readline()
    #     if not s:
    #         print('done')
    #         break
    #     print('line datas is:', s)
    # 读取多行
    L = f.readlines()
    print(L)
    f.close()
except OSError:
    print('open failure')