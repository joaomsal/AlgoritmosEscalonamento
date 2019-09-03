import processo as PRO
import fifo as FI
from multiprocessing import Process

#MULTILEVEL COM PAGINAÇÃO
def multilevel(paginas, processo):
	level2 = []
# LEVEL 1 ROUND ROBIN
	print("LEVEL 1 -> ROUND ROBIN")
	pages = processo.getPages()
	for ps in pages:
		pg = pages.pop(0)
		if pg != ' ' and pg != '':		
			t = PRO.getTempo(pg)
			p = PRO.getPage(pg)
				#if p in paginas:
			if t <= 5:
				print("EXECUTANDO PROCESSO", processo.getId(), "NA PÁGINA", p, "NO TEMPO",t)
				print("PÁGINAS NA FILA")
				print(pages)
			else:
				print("EXECUTANDO PROCESSO", processo.getId(), "NA PÁGINA", p, "NO TEMPO",t)
				pages.append(str(t-5)+":"+str(p))
				print("PÁGINAS NA FILA")
				print(pages)
				level2.append(PRO.Process(processo.getId(), pages))
# LEVEL 2 FIFO
	print("LEVEL 2 -> FIFO")
	roundRobin(level2, paginas)

#ROUND-ROBIN COM PAGINAÇÃO        
def roundRobin(paginas, pro, processos):
	pages = pro.getPages()
	while len(pages) > 0:
		pg = pages.pop(0)
		if pg != ' ' and pg != '':
				
			t = PRO.getTempo(pg)
			p = PRO.getPage(pg)

			if t <= 5:
				print("EXECUTANDO PROCESSO", pro.getId(), "NA PÁGINA", p, "NO TEMPO",t)
				print("PÁGINAS NA FILA")
				print(pages)
			else:
				print("EXECUTANDO PROCESSO", pro.getId(), "NA PÁGINA", p, "NO TEMPO",t)
				pages.append(str(t-5)+":"+str(p))
				print("PÁGINAS NA FILA")
				print(pages)
				processos.append(PRO.Process(id, pages))


def iniciaRR(processos, paginas):
	for p in processos:
		Process(target=roundRobin, args=(paginas, p, processos)).start()

def iniciaML(processos, paginas):
	for p in processos:
		Process(target=multilevel, args=(paginas, p)).start()
