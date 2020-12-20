username = 'ss'
pw = '123'

count = 0
while count < 3:
    inp_name = input('please input name:')
    inp_pw = input('please input pw:')
    if inp_name == username and inp_pw == pw:
        print('login success!')
        while True:
            cmd = input('please input cmd:')
            if cmd == 'q':
                break
            else:
                print('cmd > {s} is running'.format(s=cmd))
        break
    else:
        count += 1
        print('input error!')
else:
    print('You made a mistake three times！！！')
