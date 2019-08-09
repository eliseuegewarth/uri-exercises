
p=0
t=0
for i in range(6):
	n = float(input())
	if n > 0:
		p = p +1
		t = t + n

print("{} valores positivos".format(p))
print("{0:.1f}".format(t/p))
