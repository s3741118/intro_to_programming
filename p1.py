n = int(input('danh sach phan tu n= '))
#n = 7
range_of_list = range(0, n, 1)
list1 = []

for x in range_of_list:
    print('enter the value', x, '=')
    gt = int(input())
    list1.append(gt)

biggest = list1[0]
second_biggest = list1[1]
third_biggest = list1[2]
fourth_biggest = list1[3]

for x in list1:
    if x > biggest:
        biggest = x
print('the biggest value is ', biggest)
for x in list1:
    if biggest > x > second_biggest:
        second_biggest = x
print('the second biggest value is ', second_biggest)
for x in list1:
    if second_biggest > x > third_biggest:
        third_biggest = x
print('the third biggest value is ', third_biggest)
for x in list1:
    if third_biggest > x > fourth_biggest:
        fourth_biggest = x
print('the third biggest value is ', fourth_biggest)






