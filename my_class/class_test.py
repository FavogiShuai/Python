
class Dog:
    def eat(self, food):
        print('eat ', food)

class Cat:
    __slots__ = ['color']

    def __init__(self, color='red'):
        self.color = color
        pass

    def eat(self, food):
        print(self.color, 'cat eat', food)

    def __del__(self):
        print('对象已销毁')

if __name__ == '__main__':
    dog = Dog()
    dog.color = 'red'
    dog.eat('meat')
    print(dog.color)

    cat = Cat('black')
    cat.eat('fish')
    cat2 = Cat()
    print(cat.__slots__)