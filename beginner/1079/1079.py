
n = int(input())
for i in range(n):
	a,s,d = [float(x) for x in input().split()]
	m = (a*2 + s*3 + d*5)/(2+3+5)
	print("{0:.1f}".format(m))
