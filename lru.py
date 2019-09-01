from multiprocessing import Process

frames = []
tempo = []

def encontrarLRU(tempo, tam):
	"""Encontrar a posição do processo que foi menos utilizado"""
	tempo_minimo = tempo[0]
	posicao = 0
	for i in range(tam):
		if tempo[i] < tempo_minimo:
			tempo_minimo = tempo[i]
			posicao = i

	return posicao


def contarLRUPageFaults(nro_frames, processoID, paginas):
	'''Contar page faults de cada processo'''
	if processoID == '':
		return

	if '' in paginas:
		paginas.remove('')

	tempo = [0 for i in paginas]
	pages = []
	faults, count = (0, 0)
	frames = [-1 for x in range(nro_frames)]
	
	i = 0
	while i < len(paginas):
		flag1, flag2 = (0, 0)	
		tempo_e_pagina = paginas[i].split(':')
		tempo[i] = (int(tempo_e_pagina[0]))
		pages.append(int(tempo_e_pagina[1]))

		j = 0
		while j < nro_frames:
			if frames[j] == pages[i]:
				count += 1				
				tempo[j] = count
				flag1, flag2 = (1, 1)
				break
			j += 1			

		if flag1 == 0:
			j = 0
			while j < nro_frames:
				if (frames[j] == -1):
					count += 1
					faults += 1
					frames[j] = pages[i]
					tempo[j] = count
					flag2 = 1
					break
				j += 1
			
			
		if flag2 == 0:
			posicao = encontrarLRU(tempo, nro_frames)
			count += 1
			faults += 1
			frames[posicao] = pages[i]
			tempo[posicao] = count
			continue
				
		i += 1

	d = {'Proc': int(processoID), 'Page faults': faults}
	print(d)


def startProcessing(nro_frames, processos, paginas):
	# saidaProcessos = []

	for x in processos:
		Process(target=contarLRUPageFaults, args=(nro_frames, x.id, x.paginas,)).start()

	# return saidaProcessos
