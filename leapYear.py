def leap_year(year1):
    if year1 % 4 == 0 and year1 % 100 != 0 or year1 % 400 == 0:
        print('it is leap year')
    else:
        print('it is not leap year')


year = int(input('please enter any year to check: '))
print(leap_year(year))
