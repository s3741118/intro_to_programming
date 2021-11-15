def is_odd(number):
    from is_even import even
    if even(number):
        return False
    elif not even(number):
        return True


num = int(input('please enter an integer: '))
print(is_odd(num))
