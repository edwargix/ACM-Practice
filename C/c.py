#Kind of janky, but it works to the best of my knowledge
coord = input().splitlines()
coord = [int(x) for x in coord]
x = coord[0]
y = coord[1]
if x > 0:
	if y > 0:
		print("1")
	else:
		print("4")
else:
	if y > 0:
		print("2")
	else:
		print("3")
