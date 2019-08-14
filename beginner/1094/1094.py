
n = int(input())
r, c, s, t = [0, 0, 0, 0]
for x in range(1,n+1):
	ln = input().split()
	if ln[1] == "R":
		r = r + int(ln[0])
	elif ln[1] == "C":
		c = c + int(ln[0])
	elif ln[1] == "S":
		s = s + int(ln[0])
	else:
		pass
	t = t + int(ln[0])

print("Total: {} cobaias".format(t))
print("Total de coelhos: {}".format(c))
print("Total de ratos: {}".format(r))
print("Total de sapos: {}".format(s))
print("Percentual de coelhos: {0:.2f} %".format(c*100/t))
print("Percentual de ratos: {0:.2f} %".format(r*100/t))
print("Percentual de sapos: {0:.2f} %".format(s*100/t))
