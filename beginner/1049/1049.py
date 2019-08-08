
a = input()
b = input()
c = input()

if a in "vertebrado":
	if b in "ave":
		if c in "carnivoro":
			print("aguia")
		else:
			print("pomba")
	else:
		if c in "onivoro":
			print("homem")
		else:
			print("vaca")
else:
	if b in "inseto":
		if c in "hematofago":
			print("pulga")
		else:
			print("lagarta")
	else:
		if c in "hematofago":
			print("sanguessuga")
		else:
			print("minhoca")
