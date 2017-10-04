#Kind of janky, but it works to the best of my knowledge
import sys

for i in sys.stdin:
  coord = i.splitlines()
	coord_list = open(coord[0], 'r').read().splitlines()
	coord_list = [int(x) for x in coord_list]
	x = coord_list[0]
	y = coord_list[1]
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
	break
