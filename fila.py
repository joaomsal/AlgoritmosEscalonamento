import time
#Estrutura do processo
class Processo(object):
        def __init__(self, id, tempo, pagina):
            self.id = id
            self.tempo = tempo
            self.pagina = pagina
        
        def getId(self):
            return self.id
        
        def getTempo(self):
            return self.tempo
        
        def getPagina(self):
            return self.pagina

        
# entradas: uma fila de processos e um quantum
def roundRobin(fila, qt):
    # Se o tempo de execução for maior que o quantum
    # o processo volta pra fila
    print("----------- Round Robin -----------")
    while fila != []:
        p = fila.pop(0)
        id = p.getId()
        if p.getTempo()<=qt:
           print("Executando o processo " ,p.getId())
           time.sleep(p.getTempo())
        else:
           print("Executando o processo " ,p.getId())
           t = p.getTempo()-qt
           pa = Processo(id, t, p.getPagina)
           time.sleep(t)
           print("*O processo ", id, " deve voltar para a fila" )
           fila.append(pa)
       

def fifo(fila):
    # execução dos processos
        print("----------- Fila normal -----------")
        while fila != []:
            aux = fila.pop(0)
            print("Executando o processo: " ,aux.getId())
            time.sleep(aux.getTempo())


# multilevel, level 1: roundRobin; level 2: fifo
# entradas: uma fila de processos e um quantum
def multilevel(fila, qt):
    filaAux = []
# execução do level 1
    print("----------- MULTILEVEL -----------")
    print("LEVEL 1: Usando Round Robin")
    for p in fila:
        id = p.getId()
        if p.getTempo()<=qt:
           print("Executando o processo " ,p.getId())
           time.sleep(p.getTempo())
        else:
           print("Executando o processo " ,p.getId())
           t = p.getTempo()-qt
           pa = Processo(id, t, p.getPagina)
           time.sleep(t)
           print("*O processo ", id, " deve voltar para a fila" )
           filaAux.append(pa)

# execucao do level 2
    print("LEVEL 2: Usando FIFO")
    while filaAux != []:
            aux = filaAux.pop(0)
            print("Executando o processo " ,aux.getId())
            time.sleep(aux.getTempo())



if __name__ == "__main__":
        #Fila de processos
        fila = []
        #Processos
        p1 = Processo(1,6.30,2)
        p2 = Processo(2,4.60,5)
        p3 = Processo(3,3.90,6)
        p4 = Processo(4,9.68,9)
        p5 = Processo(5,2.30,10)
        p6 = Processo(6,1.99,12)
        #Lista dos tempos de espera de cada processo
        tempoEspera = []
        #O primeiro processo não precisa esperar
        tempoEspera.append(0)
        tempoTotal = 0
        #adição dos processos na fila
        fila.append(p1)
        fila.append(p2)
        fila.append(p3)
        fila.append(p4)
        fila.append(p5)
        fila.append(p6)
        # variáveis auxiliares
        c = 0
        ult = 0
        # Pegando o tempo de espera de cada processo na fila
        for i in fila:
            aux = i
            c+=aux.getTempo()
            tempoEspera.append(c)
        # Pegando o tempo total de espera
        for i in tempoEspera:
            tempoTotal+= i
            ult = i
        #calculando  
        tempoTotal = tempoTotal - i
        tempoMedio = tempoTotal/len(tempoEspera)
        #criando cópias da lista de processos
        fila2 = fila.copy()
        fila3 = fila.copy()
        
        #executando os algoritmos
        fifo(fila)
        roundRobin(fila2,5)
        multilevel(fila3,5)
        print("----------- RESULTADOS -----------")
        print("Tempo total esperado = ", tempoTotal)
        print("Tempo médio esperado = ", tempoMedio)

            
