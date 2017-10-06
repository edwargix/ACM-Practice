#It works, but we need to make it run faster

counter = 0
c_loop = 0
compare_number = 0
compare_number_l = {}
compare_number_right = {}
number_of_entries = int(input())
base_number = int(input())
for i in range(0,number_of_entries-1):
    c_loop = 0
    print(counter)
    compare_number = base_number
    number = int(input())
    while c_loop == 0:
        if number > compare_number and compare_number not in compare_number_right:
            compare_number_right[compare_number] = number
            counter += 1
            c_loop = 1
        elif number > compare_number and compare_number in compare_number_right:
            compare_number = compare_number_right.get(compare_number)
            counter += 1
        elif number < compare_number and compare_number not in compare_number_l:
            compare_number_l[compare_number] = number
            counter += 1
            c_loop = 1
        else:
            compare_number = compare_number_l.get(compare_number)
            counter += 1            
print(counter)
