import time
#APRESENTAÇÃO
def apresentacao():
        print("-----------------------------")
        print("SISTEMAS OPERACIONAIS")
        print("ESCALONAMENTO DE PROCESSOS")
        print("USANDO PAGINAÇÃO")
        print("-----------------------------")

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
                tempos = l.split(",")
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

# FIFO COM PAGINAÇÃO
def fifo(processos, paginas):
        print("FILA")
        while processos != []:
                pr = processos.pop(0)
                pages = pr.getPages()
                while len(pages) > 0:
                        pg = pages.pop(0)
                        if pg != ' ':
                                t = getTempo(pg)
                                p = getPage(pg)

                                if p in paginas:
                                        print("EXECUTANDO PROCESSO", pr.getId(), "NA PÁGINA", p, "NO TEMPO",t)
                                        time.sleep(t/1000)
                                        print("PÁGINAS NA FILA")
                                        print(pages)
                                else:
                                        print("ERRO: PÁGINA NÃO DISPONÍVEL")
                                        pages.append(pg)

#MULTILEVEL COM PAGINAÇÃO
def multilevel(processos, paginas):
        level2 = []
# LEVEL 1 ROUND ROBIN
        print("LEVEL 1 -> ROUND ROBIN")
        while processos != []:
                        pr = processos.pop(0)
                        pages = pr.getPages()
                        for ps in pages:
                                pg = pages.pop(0)
                                if pg != ' ':
                                        
                                        t = getTempo(pg)
                                        p = getPage(pg)


                                        #if p in paginas:
                                        if t <= 5:
                                                print("EXECUTANDO PROCESSO", pr.getId(), "NA PÁGINA", p, "NO TEMPO",t)
                                                time.sleep(t/1000000)
                                                print("PÁGINAS NA FILA")
                                                print(pages)
                                        else:
                                                print("EXECUTANDO PROCESSO", pr.getId(), "NA PÁGINA", p, "NO TEMPO",t)
                                                time.sleep(5/1000000)
                                                pages.append(str(t-5)+":"+str(p))
                                                print("PÁGINAS NA FILA")
                                                print(pages)
                                                level2.append(Process(pr.getId(), pages))
# LEVEL 2 FIFO
        print("LEVEL 2 -> FIFO")
        fifo(level2, paginas)

#ROUND-ROBIN COM PAGINAÇÃO        
def roundRobin(processos, paginas):
        while processos != []:
                pr = processos.pop(0)
                pages = pr.getPages()
                while len(pages) > 0:
                        pg = pages.pop(0)
                        if pg != ' ':
                                
                                t = getTempo(pg)
                                p = getPage(pg)


                                #if p in paginas:
                                if t <= 5:
                                        print("EXECUTANDO PROCESSO", pr.getId(), "NA PÁGINA", p, "NO TEMPO",t)
                                        time.sleep(t)
                                        print("PÁGINAS NA FILA")
                                        print(pages)
                                else:
                                        print("EXECUTANDO PROCESSO", pr.getId(), "NA PÁGINA", p, "NO TEMPO",t)
                                        time.sleep(5/1000)
                                        pages.append(str(t-5)+":"+str(p))
                                        print("PÁGINAS NA FILA")
                                        print(pages)
                                        processos.append(Process(id, pages))
                                

# MAIN ----------------------------------------    

if __name__ == "__main__":

        #CABEÇALHO
        apresentacao()
        
        #ARQUIVO DE REFERENCIA DO PROF
        arquivo = open('referencias1.txt', 'r')
        
        #LEITURA DOS DADOS DO ARQUIVO
        processos = parse(arquivo.read())
        p1 = parse(arquivo.read())
        p2 = parse(arquivo.read())

        #PAGINAS
        paginas = paginas(30)
        pg1 = paginas.copy()
        pg2 = paginas.copy()
        #ROUND-ROIBN
        roundRobin(processos,paginas)
        #MULTILEVEL
        #multilevel(processos,paginas)
        #FIFO
        fifo(processos, paginas)
                                
                                

            
