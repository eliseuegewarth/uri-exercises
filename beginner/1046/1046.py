
a, b = [int(x) for x in input().split()]

if a >= b:
	print("O JOGO DUROU {} HORA(S)".format((24-a)+b))
else:
	print("O JOGO DUROU {} HORA(S)".format(b-a))
