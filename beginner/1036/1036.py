
a,b,c = [float(x) for x in input().split()]

delta = ((b**2)-(4*a*c))
if a != 0 and delta > 0:
	sqrt_delta = (delta)**(1/2)
	r1 = (-b + sqrt_delta)/(2*a)
	r2 = (-b - sqrt_delta)/(2*a)

	print("R1 = {0:.5f}".format(r1))
	print("R2 = {0:.5f}".format(r2))

else:
	print("Impossivel calcular")
