# -*- coding: utf-8 -*-

x = input()
x = int(x)

def palavra(palavra):
	aux = ''
	nPalavra = ''
	i = 0
	m = len(palavra) / 2
	for s in palavra:
		if (ord(s) >= 65 and ord(s) <= 90) or (ord(s) >= 97 and ord(s) <= 122):
			aux = chr(ord(s) + 3)
		else:
			aux = s

		if i < m:
			aux = chr(ord(aux) - 1)
			i += 1
		nPalavra += aux

	nPalavra = ''.join(reversed(nPalavra))
	return nPalavra

txt = []
for i in range(0,x):
	t = input()
	txt.append(t)

for p in txt:
	print(palavra(p))