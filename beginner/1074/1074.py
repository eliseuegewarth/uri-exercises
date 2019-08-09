
n = int(input())
for i in range(n):
	x = int(input())
	if x == 0:
		print("NULL")
	else:
		eo = ["EVEN", "ODD"]
		np = ["NEGATIVE", "POSITIVE"]
		if x > 0:
			q = np[1]
		else:
			q = np[0]
		if x%2==0:
			w = eo[0]
		else:
			w = eo[1]
		print("{} {}".format(w, q))
