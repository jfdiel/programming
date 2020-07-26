# -*- coding: utf-8 -*-
valor = float(input())
nota = 0

print 'NOTAS:'
if valor >= 100:
	calc = valor / 100
	nota = int(calc)
	valor = valor - (nota * 100)
print str(nota)+' nota(s) de R$ 100.00'
nota = 0

if valor >= 50:
	calc = valor / 50
	nota = int(calc)
	valor = valor - (nota * 50)
print str(nota)+' nota(s) de R$ 50.00'
nota = 0

if valor >= 20:
	calc = valor / 20
	nota = int(calc)
	valor = valor - (nota * 20)
print str(nota)+' nota(s) de R$ 20.00'
nota = 0

if valor >= 10:
	calc = valor / 10
	nota = int(calc)
	valor = valor - (nota * 10)
print str(nota)+' nota(s) de R$ 10.00'
nota = 0

if valor >= 5:
	calc = valor / 5
	nota = int(calc)
	valor = valor - (nota * 5)
print str(nota)+' nota(s) de R$ 5.00'
nota = 0

if valor > 2:
	calc = valor / 2
	nota = int(calc)
	valor = valor - (nota * 2)
print str(nota)+' nota(s) de R$ 2.00'

moeda = 0
print 'MOEDAS:'
if valor >= 1:
	calc = valor / 1
	moeda = int(calc)
	valor = valor - (moeda * 1)
print str(moeda)+' moeda(s) de R$ 1.00'
moeda = 0

if valor >= 0.50:
	calc = valor - 0.50
	moeda = 1
	valor = calc
print str(moeda)+' moeda(s) de R$ 0.50'
moeda = 0

if valor >= 0.25:
	calc = valor - 0.25
	moeda = 1
	valor = calc
print str(moeda)+' moeda(s) de R$ 0.25'
moeda = 0

if valor >= 0.1:
	calc = valor / 0.1
	moeda = int(calc)
	valor = valor - (moeda * 0.1)
	valor = float(format(valor, '.2f'))
print str(moeda)+' moeda(s) de R$ 0.10'
moeda = 0

if (valor - 0.05) >= 0:
	calc = valor - 0.05
	moeda = 1
	valor = float(format(calc, '.2f'))
print str(moeda)+' moeda(s) de R$ 0.05'
moeda = 0

if valor > 0:
	moeda = valor * 100
print str(int(moeda))+' moeda(s) de R$ 0.01'
