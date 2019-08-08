
x = float(input())
rate = 0.04
if x >= 0 and x <= 400.00:
	rate = 0.15
if x > 400 and x <= 800.00:
	rate = 0.12
if x > 800 and x <= 1200.00:
	rate = 0.10
if x > 1200 and x <= 2000.00:
	rate = 0.07
else:
	pass

print("Novo salario: {0:.2f}".format(x*(1+rate)))
print("Reajuste ganho: {0:.2f}".format(x*rate))
print("Em percentual: {} %".format(int(rate*100)))
