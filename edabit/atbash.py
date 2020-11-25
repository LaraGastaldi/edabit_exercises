def atbash(txt):
	alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k' ,'l', 'm', 'n' ,'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'y', 'z']
	novo = []

	for letra in txt:
		if letra in alpha:
			idx = -(alpha.index(letra)+1)
			novo.append(alpha[idx])
		else:
			if letra == " ":
				novo.append(" ")
			else:
				letra.lower()
				idx = -(alpha.index(letra)+1)
				novo.append(alpha[idx].upper())
	return "".join(novo)

print(atbash("abcde"))