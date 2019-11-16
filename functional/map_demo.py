def my_pow(x):
    return x**2



def test_one():
    print(type(map(my_pow, range(1, 10))))
    print(sum(map(my_pow, range(1, 10))))


if __name__ == '__main__':
    test_one()