import processo as PRO
from multiprocessing import Process

# FIFO COM PAGINAÇÃO
def fifo(processo, paginas):
		pages = processo.getPages()
	
		while len(pages) > 0:
			pg = pages.pop(0)
			if pg != ' ' and pg != '':
				t = PRO.getTempo(pg)
				p = PRO.getPage(pg)

			if p in paginas:
				print("EXECUTANDO PROCESSO", processo.getId(), "NA PÁGINA", p, "NO TEMPO",t)
				print("PÁGINAS NA FILA")
				print(pages)
			else:
				print("ERRO: PÁGINA NÃO DISPONÍVEL")
				pages.append(pg)

def inicia(processos, paginas):
    for p in processos:
        x = Process(target=fifo, args=(p, paginas)).start()

