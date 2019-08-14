
maior = int(input())
indice = 1
for x in range(2,101):
	i = int(input())
	if i > maior:
		maior = i
		indice = x

print(maior)
print(indice)
