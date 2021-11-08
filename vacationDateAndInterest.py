# question 3
date = int(input('please enter a number from 0 to 6 to check the date '))
a = int(input('how many days do you travel ? '))
# if a > date:
b = a % 7 + date
if b == 1:
    print("it's Monday")
elif b == 2:
    print("it's Tuesday")
elif b == 3:
    print("it's Wednesday")
elif b == 4:
    print("it's Thursday")
elif b == 5:
    print("it's Friday")
elif b == 6:
    print("it's Saturday")

# question 4
n = 12
r = 0.08
p = float(input('please enter a principal amount ')) # principal amount
t = int(input('please enter how many years that you want for waiting to earn compound interest: '))
A = p*(1+r/n)**(n*t) # A is final money the costumer will get after waiting amount of years to earn compound interest
print('Here will be your final money after waiting a mount of years to earn compound interest: {}'.format(A))



