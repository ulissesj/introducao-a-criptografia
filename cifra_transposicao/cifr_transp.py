claro_texto = open("claro.txt", encoding="utf-8").read().replace("\n", "").replace(" ", "")
claro = []

#Separar cada palavra pelo tamanho da chave
for index in range(0, len(claro_texto), 7):
    claro.append(claro_texto[index : index + 7])

with open('cifrado.txt', 'w') as f:
        for item in claro:
            f.write("%s\n" %item)

#Transpoe o texto tranformando as linhas em colunas
#texto1 a ser transposto e texto2 como saida
def transpor_texto(texto1, texto2):
	for x in zip(*texto1): #funcao zip para transpor a matriz, pareia os characteres com as colunas na sua posição
		for y in x:
			print(y, end='', file = texto2)
		print(' ', file=texto2) 
	texto2.close()


saida = []
saida_decif = []
#Inicializa vetor saida com 0 nas 7 posições 
def ini_vet(vet):
	for x in range(7):
		vet.append(0) 

ini_vet(saida)
ini_vet(saida_decif)
#Faz a translação de acordo com a sequência
#Parametros são o vetor de dígitos e o vetor de texto claro
def encript(vetor_digitos, texto):
    for x in range(7):
        pos = vetor_digitos[x] - 1 #Pega a posição que o texto vai estar no vetor
        saida[pos] = texto[x] #atribui a posição da saída
    return saida 

#Decrifrar o texto, fazer este processo 3 vezes
def decript(vetor_digitos, texto):
	for x in range(7):
		pos = x+1 #Guarda o digito(1-7)
		for y in range(7):
			if vetor_digitos[y] == pos: #Procura pela posicao do digito que está no vetor
				saida_decif[y] = texto[x] #atribui a posição desse digito na saída
	return saida_decif

chave = input("Digite a chave de 7 digitos(de 1-7 sem repetições e sem espaços): ") 
digitos = [int(d) for d in str(chave)]


input("Aperte enter para cifrar...")
print("Cifrando...")

""""CIFRAR"""
for i in range(3):
    claro_aux = open('cifrado.txt', 'r')
    aux_texto = open('aux_texto.txt', 'w')
    transpor_texto(claro_aux, aux_texto)

    transposto = open('aux_texto.txt', 'r').read().replace("\n", "").replace(" ", "")
    transposto_lista = []
    for index in range(0, len(transposto), len(claro)):
        transposto_lista.append(transposto[index : index + len(claro)])
    #print(transposto)
    #print(transposto_lista)

    res = encript(digitos, transposto_lista)
    with open('cifrado.txt', 'w') as f:
            for item in res:
                f.write("%s\n" %item)
    
    cifr_transp = open('cifrado.txt', 'r').read().replace("\n", "").replace(" ", "")

    #print(cifr_transp)
    nova_lista =[]
    for index in range(0, len(cifr_transp), 7):
        nova_lista.append(cifr_transp[index : index + 7])
    
    with open('cifrado.txt', 'w') as f:
            for item in nova_lista:
                f.write("%s\n" %item)
    
    if(i==2):
        with open('cifrado.txt', 'w') as f:
                for item in nova_lista:
                    f.write("%s" %item)
        with open('aux_texto.txt', 'w') as f:
                for item in nova_lista:
                    f.write("%s" %item)

print("Texto cifrado em cifrado.txt!\n")
print(nova_lista)

input("Aperte enter para decifar...")
print("Decifrando...")

cifrado = []
cifrado_texto = open("cifrado.txt").read().replace("\n", "").replace(" ", "")
#Separar cada palavra pelo tamanho da chave
for index in range(0, len(cifrado_texto), 7):
    cifrado.append(cifrado_texto[index : index + 7])

with open('decifrado.txt', 'w') as f:
        for item in cifrado:
            f.write("%s\n" %item)

""""DECIFRAR"""
for i in range(3):
    transposto = open('decifrado.txt', 'r').read().replace("\n", "").replace(" ", "")
    transposto_lista = []
    for index in range(0, len(transposto), len(claro)):
        transposto_lista.append(transposto[index : index + len(claro)])
    
    #print(transposto_lista)
    res = decript(digitos, transposto_lista)
    #print(res)
    with open('decifrado.txt', 'w') as f:
            for item in res:
                f.write("%s\n" %item)

    cif_aux = open('decifrado.txt', 'r')
    aux_texto = open('aux_texto.txt', 'w')

    transpor_texto(cif_aux, aux_texto)
    
    cifr_transp = open('aux_texto.txt', 'r').read().replace("\n", "").replace(" ", "")

    nova_lista =[]
    for index in range(0, len(cifr_transp), 7):
        nova_lista.append(cifr_transp[index : index + 7])
    #print(nova_lista)
    with open('decifrado.txt', 'w') as f:
            for item in nova_lista:
                f.write("%s\n" %item)
    
    if(i==2):
        with open('decifrado.txt', 'w') as f:
                for item in nova_lista:
                    f.write("%s" %item)
    
print("Texto decifrado em decifrado.txt!")
print(nova_lista)
