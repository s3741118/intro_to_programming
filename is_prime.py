def prime(num1):
    if num1 % num1 == 0 and num1 % 2 != 0 and num1 % 3 != 0:
        print('it is a prime number')
    elif num1 == 2:
        print('it is a prime number')
    elif num1 == 3:
        print('it is a prime number')
    else:
        return False


num = int(input('Please enter an integer: '))
print(prime(num))
