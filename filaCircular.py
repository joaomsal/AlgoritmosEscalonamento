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

#True = 1 e False = 0
def filaCircular(paginas, processos):
    pages = inicializaPaginas(paginas)

    while processos != []:
        pe = processos.pop(0)
        pg = pe.getPages()
        while pg !=[]:
            pg0 = pg.pop(0)
            for p in pages:
                if not p[1]:
                    p[1] = True
                    if pg0 != ' ':
                        time.sleep(getTempo(pg0)/1000000)
                        print("Executando o processo", pe.getId())
                else: 
                    p[1] = False 
                    print("SEM PÁGINAS DISPONÍVEIS")
