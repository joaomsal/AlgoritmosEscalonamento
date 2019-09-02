import time
import fila as FL

def inicializaPaginas(paginas):
    pages = []
    for p in paginas:
        aux = []
        aux.append(p)
        aux.append(False)
        pages.append(aux)

    return pages

def getTempo(tp):
	if tp !=[]:
		aux = tp.split(":")
		t = aux.pop(0)

		if t != ' ':
			return int(t)
		else:
			return 0

def getPage(tp):
	if len(tp) > 0:
		aux = tp.split(":")
		aux.pop(0)
		p = aux.pop(0)

	if p != ' ':
		return int(p)
	else:
		return 0

def alcoc(p, pages):
    r = False
    for i in pages:
        if i[0] == p[0]:
            r = True
    return r

#True = 1 e False = 0
def filaCircular(paginas, processos):
    pages = inicializaPaginas(paginas)
    i = 0
    while processos != []:
        pe = processos.pop(0)
        pg = pe.getPages()
        while pg !=[]:
            pg0 = pg.pop(0)
            for p in pages:
                if not p[1] and alcoc(p, pages):
                    print(p, pages)
                    if pg0 != ' ':
                        p[1] = True
                        p[0] = getPage(pg0)
                        time.sleep(getTempo(pg0)/1000000)
                        print("Executando o processo", pe.getId())
                else: 
                    p[1] = False 
                    i+=1
                    print("SEM PÁGINAS DISPONÍVEIS -> FALTAS = ", i)
                                   
