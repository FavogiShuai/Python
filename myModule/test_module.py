from myModule import my_module1
import random
help(my_module1)
my_module1.say_hello()
my_module1.new_func()
l = []
i = 7
while i > 0:
    x = 0
    if i < 6:
        x = random.randint(1, 33)
    else:
        x = random.randint(1, 16)
    if x not in l:
        l.append(x)
        i -= 1
print(l)
