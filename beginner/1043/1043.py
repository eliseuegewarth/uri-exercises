
a, b, c = [float(x) for x in input().split()]
if a + b > c and b + c > a and c + a > b:
	print("Perimetro = {0:.1f}".format(a+b+c))
else:
	print("Area = {0:.1f}".format(c*(a+b)/2))
