def my_deco(fn):
    def fx():
        print('++++++++')
        fn()
        print('--------')
    return fx


@my_deco
def my_func():
    print('my_func被调用')


def message(fx):
    # print('initial')

    def fn(name, x):
        fx(name, x)
        print('消息:银行卡余额变动')
    return fn


@message
def save_money(name, x):
    print(name, '存钱', x, '元')


@message
def withdraw(name, x):
    print(name, '取钱', x, '元')


if __name__ == '__main__':
    my_func()

    save_money('jack', 500)
    withdraw('tom', 1000)
