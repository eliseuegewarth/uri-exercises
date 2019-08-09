
n = int(input())
ii=0
oi=0
for i in range(n):
	h = int(input())
	if h >= 10 and h <= 20:
		ii = ii + 1
	else:
		oi = oi + 1
print("{} in".format(ii))
print("{} out".format(oi))
