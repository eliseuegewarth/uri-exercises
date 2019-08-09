
l = []
for i in range(5):
	l.append(int(input()))
par = 0
for i in l:
	if i%2==0:
		par = par + 1

print("{} valores pares".format(par))
