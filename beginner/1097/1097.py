x = 5
for i in range(1,10, 2):
	for j in reversed(range(x, x+3)):
		print("I={} J={}".format(i,j))
	x = x + 2
