
l = []
for i in range(5):
	l.append(int(input()))
par = 0
impar = 0
positivo = 0
negativo = 0
for i in l:
	if i%2==0:
		par = par + 1
	else:
		impar = impar + 1
	if i > 0:
		positivo = positivo + 1
	elif i == 0:
		pass
	else:
		negativo = negativo + 1
print("{} valor(es) par(es)".format(par))
print("{} valor(es) impar(es)".format(impar))
print("{} valor(es) positivo(s)".format(positivo))
print("{} valor(es) negativo(s)".format(negativo))
