import time
str = "10 + 20 加 减乘除"
L = str.split()
print(L)
print(L[-1::-2])


def fx(a, b, c):
    print(a, b, c)


if __name__ == '__main__':
    my_dict = {"a": 10, "b": 20, "c": 30}
    fx(*my_dict)

    print(time.strftime('%Y-%m-%d', time.localtime(1477471508)))