def my_range(start, stop=None, step=1):
    l = []
    # 只传入一个参数
    if stop is None:
        stop = start
        start = 0
    i = start
    while i < stop:
        l.append(i)
        i += step
    return l


if __name__ == '__main__':
    print(my_range(3))
    print(my_range(3, 8))
    print(my_range(5, 20, 5))
