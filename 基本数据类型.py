age = 18
# 格式化
res = 'my name is %s,my age is %s' % ('shuaishuai', '18')
print(res)
res1 = 'my name is {},my age is {}'.format('shuaishuai', '18')
print(res1)


name = 'shuaishuai'
age = 18
res2 = f'my name is {name},my age is {18}'
print(res2)

m = 20
n = 10
m = m + n
n = m - n
m = m - n
print(m, n)

l = [1, 2, 3, 4]
l1 = l.copy()
l1[0] = 5
print(l)
