
x = float(input())
if x > 0 and x <= 2000:
	print("Isento")
elif x > 2000 and x <= 3000:
	print("R$ {0:.2f}".format((x-2000)*0.08))
elif x > 3000 and x <= 4500:
	print("R$ {0:.2f}".format((x-3000)*0.18+(1000*0.08)))
elif x >  4500:
	print("R$ {0:.2f}".format((x-4500)*0.28 + (1500*0.18)+(1000*0.08)))
