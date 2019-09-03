import time
import lru as LRU
import optimal as OPTIMAL
import clock as CL
import escalonamento as ES
import processo as PRO
import fifo as FI

#APRESENTAÇÃO
def apresentacao():
        print("-----------------------------")
        print("SISTEMAS OPERACIONAIS")
        print("ESCALONAMENTO DE PROCESSOS")
        print("USANDO PAGINAÇÃO")
        print("-----------------------------")
		
frames20 = 20
frames30 = 30
					
# MAIN ----------------------------------------    
if __name__ == "__main__":

	#CABEÇALHO
	apresentacao()
	
	#ARQUIVO DE REFERENCIA DO PROF
	arquivo = open('referencias1.txt', 'r')
	
	#LEITURA DOS DADOS DO ARQUIVO
	processos = PRO.parse(arquivo.read())

	#PAGINAS
	paginas = PRO.paginas(30)

	#ROUND-ROIBN
	ES.iniciaRR(processos,paginas)
	#MULTILEVEL
	ES.iniciaML(processos,paginas)
	#FIFO
	FI.inicia(processos, paginas)
	
	#LRU
	print("LRU")
	output = LRU.startProcessing(frames30, processos, paginas)
	print(output)
	print("-----------------")
	#OTIMO
	print("ótimo")
	output2 = OPTIMAL.startProcessing(frames30, processos)
	print(output2)
	print("-----------------")
	#CLOCK
	print("CLOCK")
	CL.inicia(processos, paginas)
	print("-----------------")
	

