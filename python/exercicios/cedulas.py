# -*- coding: utf-8 -*-

valor = input()
valor = int(valor)

notas = [100, 50, 20, 10, 5, 2, 1]

print(valor)
for n in notas:
	nota = 0
	if valor >= n:
		calc = valor / n
		nota = int(calc)
		valor = valor - (nota * n)
	print(str(nota)+' nota(s) de R$ '+str(n)+',00')