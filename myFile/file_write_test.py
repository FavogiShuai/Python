
# w : 没有文件会创建文件，如果原文件有内容会清空
f = open('./myNote.txt', 'w')
f.writelines('firstline\nsecondline\n')
f.write('hello')
f.close()

f2 = open('./myNote.txt', 'a')
f2.write(' world')
f2.close()