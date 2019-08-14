
for i in range(0, 21, 2):
	for j in range(1, 4):
		a = i/10
		if i%10==0:
			a = int(a)
		else:
			pass
		b = j+a
		print("I={} J={}".format(a,b))
