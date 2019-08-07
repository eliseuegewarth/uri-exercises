
total = 0
for i in range(2):
	x,y,z = input().split(' ')
	total = total + (int(y)*float(z))

print("VALOR A PAGAR: R$ {0:.2f}".format(total))
