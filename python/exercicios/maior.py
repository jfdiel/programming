# -*- coding: utf-8 -*-

a, b, c = raw_input().split()

a = int(a)
b = int(b)
c = int(c)

maior = ((a + b) + abs(a-b)) / 2
maior = ((maior + c) + abs(maior-c)) / 2

print(str(maior) + " eh o maior")