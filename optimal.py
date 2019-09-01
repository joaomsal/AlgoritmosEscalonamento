from multiprocessing import Process


frames = []
tempos = []
pages = []


def prox_espaco_livre(nro_frames, indice, pages):
    indice += 1
    prox = indice
    resultado = 0
    
    i = 0
    while i < nro_frames:
        j = 0
        while j < len(pages):
            if frames[i] == pages[j]:
                if j > prox:
                    prox = j
                    resultado = i
            break

        if j == len(pages) - 1:
            return i
        j += 1

        i += 1

    return resultado


def paginaOtima(nro_frames, processoID, paginas):
    if processoID == '':
        return

    if '' in paginas:
        paginas.remove('')
    
    frames = []

    i = 0
    pagina_encontrada = 0
    while i < len(paginas):
        tempo_e_pagina = paginas[i].split(':')
        pages.append(int(tempo_e_pagina[1]))
        
        if pages[i] in frames:
            pagina_encontrada += 1
            i += 1
            continue

        if (len(frames) < nro_frames):
            frames.append(pages[i])
        else:
            j = prox_espaco_livre(nro_frames, i, pages)
            frames[j] = pages[i]

        i += 1

    d = {'Proc': int(processoID), 'Page faults': len(paginas) - pagina_encontrada}
    print(d)
    #print("Faults: ", len(paginas) - pagina_encontrada)

def startProcessing(nro_frames, processos):
    for p in processos:
        paginaOtima(nro_frames, p.id, p.paginas)