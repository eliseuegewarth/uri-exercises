
a, b = [int(x) for x in input().split()]

resto = 0
if a > b:
	resto = a%b
else:
	resto = b%a

if resto == 0:
	print("Sao Multiplos")
else:
	print("Nao sao Multiplos")
