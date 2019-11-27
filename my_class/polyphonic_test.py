class Shape:
    def draw(self):
        print('Shape.draw 被调用')
class Circle(Shape):
    def draw(self):
        print('正在画一个圆')

class Point(Shape):
    def draw(self):
        print('正在画一个点')

def my_draw(obj):
    obj.draw()

if __name__ == '__main__':
    c = Circle()
    p = Point()
    my_draw(c)
    my_draw(p)