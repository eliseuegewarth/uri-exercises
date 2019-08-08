
a,b,c = sorted([float(x) for x in input().split()], reverse=True)

if a >= b + c:
	print("NAO FORMA TRIANGULO")
else:
	if a**2 == (b**2 + c**2):
		print("TRIANGULO RETANGULO")
	elif a**2 > (b**2 + c**2):
		print("TRIANGULO OBTUSANGULO")
	elif a**2 < (b**2 + c**2):
		print("TRIANGULO ACUTANGULO")
	if a == b == c:
		print("TRIANGULO EQUILATERO")
	elif a == b or b == c or a == c:
		print("TRIANGULO ISOSCELES")
