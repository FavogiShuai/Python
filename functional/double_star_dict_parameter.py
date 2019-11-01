def func(**kwargs):
    print("关键字参数个数是：", len(kwargs))
    print(kwargs)


if __name__ == '__main__':
    func(name="favo", age=18)