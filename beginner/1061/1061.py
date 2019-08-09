
dias = [[], []]

for x in range(2):
	dias[x].append(int(input().split()[1]))
	[dias[x].append(int(i.replace(' ', ''))) for i in input().split(':')]

d = dias[1][0] - dias[0][0]
h = dias[1][1] - dias[0][1]
if h < 0:
	h = h + 24
	d = d - 1
m = dias[1][2] - dias[0][2]
if m < 0:
	m = m + 60
	h = h - 1
s = dias[1][3] - dias[0][3]
if s < 0:
	s = s +60
	m = m - 1

print("{} dia(s)".format(d))
print("{} hora(s)".format(h))
print("{} minuto(s)".format(m))
print("{} segundo(s)".format(s))
