
n = [float(x) for x in input().split()]
p = [2, 3, 4, 1]

total = 0

for i in range(len(n)):
	total = total + (n[i] * p[i])
total = total/sum(p)

print("Media: {0:.1f}".format(total))
if total < 5.0:
	print("Aluno reprovado.")
elif total >= 7.0:
	print("Aluno aprovado.")
elif total >= 5.0 and total < 7.0:
	exame = float(input())
	print("Aluno em exame.")
	print("Nota do exame: {0:.1f}".format(exame))
	total = (total + exame)/2
	if total >= 5.0:
		print("Aluno aprovado.")
	else:
		print("Aluno reprovado.")
	print("Media final: {0:.1f}".format(total))
