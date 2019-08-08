
a, b, c, d = [int(x) for x in input().split()]

h = c - a
m = d - b
if m < 0:
	m = m + 60
	h = h - 1
if h < 0 or (m == 0 and h == 0):
	h = h + 24

print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(h, m))
