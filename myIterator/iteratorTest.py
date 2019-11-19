l = [1, 2, 3, 4, 5]
it = iter(l)
print(next(it))

while True:
    try:
        print(next(it))
    except StopIteration:
        print('None')
        break