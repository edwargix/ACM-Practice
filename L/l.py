n = int(input())

for _ in range(n):
    line = input()
    nums = line.split(' ')

    no_advertise = float(nums[0])
    advertise = float(nums[1])
    advertise_costs = float(nums[2])

    if no_advertise == advertise - advertise_costs:
        print("does not matter")
    elif no_advertise >= advertise - advertise_costs:
        print("do not advertise")
    else:
        print("advertise")
