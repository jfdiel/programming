# -*- coding: utf-8 -*-

nome = raw_input()
salario = float(input())
vendas = float(input())

total = (vendas * 0.15) + salario

print("TOTAL = R$ "+str(format(total, '.2f')))