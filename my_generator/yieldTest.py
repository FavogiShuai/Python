# 生成器函数
def my_yield():
    yield 2
    yield 3
    yield 5
print(my_yield())
for i in my_yield():
    print(i)