# ESTRUTURA DO PROCESSO
class Process(object):
	def __init__(self, id, paginas):
		self.id = id
		self.paginas = paginas

	def getId(self):
		return self.id

	def getPages(self):
		return self.paginas

# FAZ A LEITURA DO ARQUIVO DE PROCESSOS
def parse(entrada):
	texto = entrada.split("\n")
	processos = []
	print("LENDO ARQUIVO...")
	for l in texto:
		tempos = l.split(", ")
		id = tempos.pop(0)
		p = Process(id,tempos)
		processos.append(p)
		#print("ID = ", id)
		#print("TEMPO:PÁGINA",tempos)

	return processos

#INICIALIZA AS PÁGINAS
def paginas(n):
	pages = []

	for i in range(n):
		pages.append(i)

	return pages

#PEGA TEMPO DA ENTRADA
def getTempo(tp):
	if tp !=[]:
		aux = tp.split(":")
		t = aux.pop(0)

		if t != ' ':
			return int(t)
		else:
			return 0

#PEGA PÁGINA DA ENTRADA
def getPage(tp):
	if len(tp) > 0:
		aux = tp.split(":")
		aux.pop(0)
		p = aux.pop(0)

	if p != ' ':
		return int(p)
	else:
		return 0
