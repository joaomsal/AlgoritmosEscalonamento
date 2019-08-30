import time
#Estrutura do processo
##class Processo(object):
##    def __init__(self, id, tempoPagina):
##        self.id = id
##        self.tempoPagina = tempoPagina
##
##    def getId(self):
##        return self.id
##
##    def getTempoPagina(self):
##        return self.tempoPagina
##
###Estrutura da paginação do processo
##class TempoPagina(object):
##    def __init__(self, tempo, pagina):
##        self.tempo = tempo
##        self.pagina = pagina
##
##    def getTempo(self):
##        return self.tempo
##
##    def getPagina(self):
##        return self.pagina
##
###Memória física simulada
###é composta por blocos
##class Memoria(object):
##    def __init__(self, blocos):
##        self.blocos = blocos
##        
##    def getBlocos(self):
##        return self.blocos
##
###ESTRUTURA DO BLOCO DE MEMÓRIA
###CONTÉM O ENDEREÇO E UMA FLAG (DISPONIBILIDADE)
##class Bloco(object):
##    def __init__(self, end, flag):
##        self.end = end
##        self.flag = flag
##
##    def getEnd(self):
##        return self.end
##
##    def getFlag(self):
##        return self.flag
##
### ESTRUTURA DE PÁGINA
### CONTÉM UM ENDEREÇO DE MEMÓRIA LÓGICA E UM ENDEREÇO DE MEMÓRIA FÍSICA
##class Pagina(object):
##    def __init__(self, id, paginaLog, paginaFis):
##        self.paginaLog = paginaLog
##        self.paginaFis = paginaFis
##        self.id = id
##
##    def getPaginaLog(self):
##        return self.paginaLog
##
##    def getPaginaFis(self):
##        return self.paginaFis
##
##    def getId(self):
##        return self.id
##
##
###FUNÇÕES -----------------------------------------
##    
### entradas: uma fila de processos e um quantum
##def roundRobin(fila, qt):
##    # Se o tempo de execução for maior que o quantum
##    # o processo volta pra fila
##    print("----------- Round Robin -----------")
##    while fila != []:
##        p = fila.pop(0)
##        id = p.getId()
##        if p.getTempo()<=qt:
##           print("Executando o processo " ,p.getId())
##           time.sleep(p.getTempo())
##        else:
##           print("Executando o processo " ,p.getId())
##           t = p.getTempo()-qt
##           pa = Processo(id, t, p.getPagina)
##           time.sleep(t)
##           print("*O processo ", id, " deve voltar para a fila" )
##           fila.append(pa)
##       
##
### FILA
##def fifo(fila):
##    # execução dos processos
##        print("----------- Fila normal -----------")
##        while fila != []:
##            aux = fila.pop(0)
##            print("Executando o processo: " ,aux.getId())
##            time.sleep(aux.getTempo())
##
##
### FIFO COM PAGINAÇÃO            
##def fifo2(paginas, memoria):
##        print("EXECUTANDO FIFO COM PAGINAÇÃO")
##        while paginas !=[]:
##
##                p = paginas.pop(0)
##
##                if p.getPagina() in memoria:
##                        print(p.getPagina().getPaginaLog(), p.getPagina().getPaginaFis())
##                        time.sleep(p.getTempo())
##                else:
##                        print("voltou")
##                        paginas.append(p)
##        
##        
##
### multilevel, level 1: roundRobin; level 2: fifo
### entradas: uma fila de processos e um quantum
##def multilevel(fila, qt):
##    filaAux = []
### execução do level 1
##    print("----------- MULTILEVEL -----------")
##    print("LEVEL 1: Usando Round Robin")
##    for p in fila:
##        id = p.getId()
##        if p.getTempo()<=qt:
##           print("Executando o processo " ,p.getId())
##           time.sleep(p.getTempo())
##        else:
##           print("Executando o processo " ,p.getId())
##           t = p.getTempo()-qt
##           pa = Processo(id, t, p.getPagina)
##           time.sleep(t)
##           print("*O processo ", id, " deve voltar para a fila" )
##           filaAux.append(pa)
##
### execucao do level 2
##    print("LEVEL 2: Usando FIFO")
##    while filaAux != []:
##            aux = filaAux.pop(0)
##            print("Executando o processo " ,aux.getId())
##            time.sleep(aux.getTempo())
##
##
###inicia memoria com os blocos
##def iniciaMemoria(qt):
##    blocos = []
##    for i in range(qt):
##        if i%2 == 0:
##            aux = Bloco(i, True)
##            blocos.append(aux)
##        else:
##            aux = Bloco(i, False)
##            blocos.append(aux) 
##
##    return Memoria(blocos)
##    
##
###MONTA AS PÁGINAS COM BASE NOS BLOCOS DE MEMÓRIA DISPONIVEIS
##def pagina(memoria, qt):
##    paginas = []
##    for b in memoria.getBlocos():
##        if b.getFlag():
##            for i in range(qt):
##                paginas.append(Pagina(i, b.getEnd(), b.getEnd()+100 ))
##
##    return paginas


def apresentacao():
        print("-----------------------------")
        print("SISTEMAS OPERACIONAIS")
        print("ESCALONAMENTO DE PROCESSOS")
        print("USANDO PAGINAÇÃO")
        print("-----------------------------")


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

def getTempo(tp):
        if tp !=[]:
                aux = tp.split(":")
                t = aux.pop(0)

                if t != ' ':
                        return int(t)
                else:
                        return 0

def getPage(tp):  
        if tp !=[]:
                aux = tp.split(":")
                aux.pop(0)
                p = aux.pop(0)
                if p != ' ':
                        return int(p)
                else:
                        return 0

# FIFO COM PAGINAÇÃO
def fifo(processos, paginas):
        while processos != []:
                pr = processos.pop(0)
                pages = pr.getPages()
                for pg in pages:
                        pg = pages.pop(0)
                        t = getTempo(pg)
                        p = getPage(pg)

                        if p in paginas:
                                print("EXECUTANDO PROCESSO", pr.getId(), "NA PÁGINA", p, "NO TEMPO",t)
                                time.sleep(t/1000)
                        else:
                                pages.append(pg)
#ROUND-ROBIN COM PAGINAÇÃO        
def roundRobin(processos, paginas):
        while processos != []:
                pr = processos.pop(0)
                pages = pr.getPages()
                for pg in pages:
                        pg = pages.pop(0)
                        t = getTempo(pg)
                        p = getPage(pg)

                        #if p in paginas:
                        if t <= 5:
                                print("EXECUTANDO PROCESSO", pr.getId(), "NA PÁGINA", p, "NO TEMPO",t)
                                time.sleep(t)
                        else:
                                print("EXECUTANDO PROCESSO", pr.getId(), "NA PÁGINA", p, "NO TEMPO",t)
                                time.sleep(5/1000)
                                pages.append(str(t-5)+str(p))
                                

# MAIN ----------------------------------------    

if __name__ == "__main__":

        #CABEÇALHO
        apresentacao()
        
        #ARQUIVO DE REFERENCIA DO PROF
        arquivo = open('referencias1.txt', 'r')
        
        #LEITURA DOS DADOS DO ARQUIVO
        processos = parse(arquivo.read())
        
        #PAGINAS
        paginas = paginas(30)

        #ROUND-ROIBN
        roundRobin(processos,paginas)
        print("FIFO")
        #FIFO
        fifo(processos, paginas)
                                
                                
 # ANTIGO -------------------------------------------------------------                    

##        #processos
##        processos = []
##
##        for i in range(10):
##                temps = []
##                for j in range(5):
##                        tp = TempoPagina(1+i+j, paginas.pop(0))
##                        temps.append(tp)
##                p = Processo(i, temps)
##                processos.append(p)
##        
##
##
##
##        for p in processos:
##                id = p.getId()
##                pags = p.getTempoPagina()
##                fifo2(pags, paginas)
##                for pg in pags:       
##                        print(id, pg.getTempo(),":",pg.getPagina().getPaginaLog())
##
##                        
##        
       

        
##        #Fila de processos
##        fila = []
##        #Processos
##        p1 = Processo(1,6.30,2)
##        p2 = Processo(2,4.60,5)
##        p3 = Processo(3,3.90,6)
##        p4 = Processo(4,9.68,9)
##        p5 = Processo(5,2.30,10)
##        p6 = Processo(6,1.99,12)
##        #Lista dos tempos de espera de cada processo
##        tempoEspera = []
##        #O primeiro processo não precisa esperar
##        tempoEspera.append(0)
##        tempoTotal = 0
##        #adição dos processos na fila
##        fila.append(p1)
##        fila.append(p2)
##        fila.append(p3)
##        fila.append(p4)
##        fila.append(p5)
##        fila.append(p6)
##        # variáveis auxiliares
##        c = 0
##        ult = 0
##        # Pegando o tempo de espera de cada processo na fila
##        for i in fila:
##            aux = i
##            c+=aux.getTempo()
##            tempoEspera.append(c)
##        # Pegando o tempo total de espera
##        for i in tempoEspera:
##            tempoTotal+= i
##            ult = i
##        #calculando  
##        tempoTotal = tempoTotal - i
##        tempoMedio = tempoTotal/len(tempoEspera)
##        #criando cópias da lista de processos
##        fila2 = fila.copy()
##        fila3 = fila.copy()
##        
##        #executando os algoritmos
##        fifo(fila)
##        roundRobin(fila2,5)
##        multilevel(fila3,5)
##        print("----------- RESULTADOS -----------")
##        print("Tempo total esperado = ", tempoTotal)
##        print("Tempo médio esperado = ", tempoMedio)

            
