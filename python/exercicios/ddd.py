#ddd
def verifica(i):
	local={
		61:'Brasilia',
		71:'Salvador',
		11:'Sao Paulo',
		21:'Rio de Janeiro',
		32:'Juiz de Fora',
		19:'Campinas',
		27:'Vitoria',
		31:'Belo Horizonte'
	}
	return local.get(i,"DDD nao cadastrado")

i = input()
print verifica(i)
	