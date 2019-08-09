
import sys

months = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for i in sys.stdin:
	dias = 0
	m, d = [int(x) for x in i.split()]
	if m == 12 and d == 24:
		print("{}".format("E vespera de natal!"))
	elif m == 12 and d == 25:
		print("{}".format("E natal!"))
	elif m == 12 and d > 25:
		print("{}".format("Ja passou!"))
	elif m == 12 and d < 24:
		print("Faltam {} dias para o natal!".format(25-d))
	else:
		for f in range(m+1, 12):
			dias = dias + (months[f])
		dias = dias + (months[m]-d) + 25
		print("Faltam {} dias para o natal!".format(dias))
