a = int(input("enter a number "))
b = int(input("enter a number "))
c = int(input("enter a number "))
a2 = pow(a, 2)
b2 = pow(b, 2)
c2 = pow(c, 2)

if a+b > c and a+c > b and b+c > a:
    print('{} {} {} are three edges of a triangle'.format(a, b, c))
    if a2 + b2 == c2 or a2 + c2 == b2 or b2 + c2 == a2:
        print('it is a right triangle')
    elif a == b and a != c or a == c and a != b or b == c and b != a:
        print('it is an isosceles triangle')
    elif a == b == c:
        print('it is equilateral triangle')
    else:
        print('it is a normal triangle')
else:
    print('it is not a triangle')




