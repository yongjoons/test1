try :
    num=int(input('enter : '))


    print(10/num)
except ZeroDivisionError :
    print('zero')
except ValueError:
    print('num is not int')
