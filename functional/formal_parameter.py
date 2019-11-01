def func(*args):
    print("参数个数：", len(args))
    print("args=", args)


if __name__ == '__main__':
    func(1, 2, 3, 4, 5)