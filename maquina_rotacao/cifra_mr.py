#Pega os cilindros, uma letra e o alfabeto e determina qual será a saída
def encript(cilindro1, cilindro2, cilindro3, letra, alfabeto):
    for a in range(26):
        if letra == alfabeto[a]:
            pos_letra = a
            break

    for x in range(26):
        if(pos_letra+1) == cilindro1[x]:
            pos = x
            break
    
    for x in range(26):
        if(pos+1) == cilindro2[x]:
            prox = x+1
            break

    for x in range(26):
        if(prox) == cilindro3[x]:
            pos = x
            break
    
    prox = alfabeto[pos]
    return prox

#Decifragem da letra, processo inverso começando pelo cilindro 3
def decript(cilindro1, cilindro2, cilindro3, letra, alfabeto):
    for a in range(26):
        if letra == alfabeto[a]:
            pos_letra = a
            break
    
    #Pega a posição da letra para comparar nos cilindros
    prox = cilindro3[pos_letra]
    ligacao = cilindro2[prox-1]
    prox = cilindro1[ligacao-1]
    
    return alfabeto[prox-1] #Retorna a posição da letra

#Rotacao para direita
def rotacao_direita(cilindro):
    cilindro = (cilindro[-1:] + cilindro[:-1])
    #montar_cilindro(chave, cilindro)
    #cilindro = (cilindro[-1:] + cilindro[:-1])
    return cilindro

#Rotacao para esquerda
def rotacao_esquerda(cilindro):
    cilindro = (cilindro[1:] + cilindro[:1])
    return cilindro

def iniciar_cilindro(cilindro):
    for i in range(26):
        cilindro.append(0)

def montar_cilindro(chave, cilindro):
    for x in range(len(chave)):
        pos = chave[x]
        cilindro[pos-1] = x+1
        

def main():
    chave_1 = [4, 7, 23, 1, 2, 8 ,14 ,12 ,21 ,3 ,5 ,17 ,19 ,26 ,6 ,11 ,9 ,22 ,24 ,10 ,
    13 ,18 ,15,20,16,25]
    chave_2 = [18, 7, 6, 2, 24, 5, 23, 10, 12, 14, 15, 25, 13, 3, 21, 19, 4, 16, 20, 11,
    8, 22, 1, 9, 17, 26]
    chave_3 = [15, 19, 4, 6, 5, 11, 25, 14, 12, 21, 18, 13, 7, 23, 3, 20, 2, 8, 17, 1, 22,
    9, 26, 10, 16, 24]

    prim_cilindro = []
    seg_cilindro = []
    ter_cilindro = []
    
    iniciar_cilindro(prim_cilindro)
    iniciar_cilindro(seg_cilindro)
    iniciar_cilindro(ter_cilindro)
    
    montar_cilindro(chave_1,prim_cilindro)
    montar_cilindro(chave_2,seg_cilindro)
    montar_cilindro(chave_3,ter_cilindro)
    
    print("Cilindros: ")
    print(prim_cilindro)
    print(seg_cilindro)
    print(ter_cilindro)

    alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I','J','K','L','M','N','O','P','Q','R',
    'S','T','U','V','W','X','Y','Z']

    claro = open("claro.txt").read() #LE O ARQUIVO SEM ESPAÇOS E QUEBRAS DE LINHA
    letras = [str(d) for d in claro] #Separa o texto cada caractere e coloca em uma lista

    cifrado = []
    aux = []
    trigger = 25 #Variavel trigger segundo cilindro
    trigger3 = 675 #Variavel trigger do terceiro cilindro 
    ultima = 0 #Pega o ultimo cilindro rotacionado - 1,2 ou 3

    input("Aperte enter para cifrar...")
    print("Cifrando...\n")
    print("Rotações: ")

    """Cifrar o texto"""
    for i in range(len(letras)):
        e = letras[i]
        saida = encript(prim_cilindro,seg_cilindro,ter_cilindro,e,alfabeto)
        aux = rotacao_direita(prim_cilindro)
        prim_cilindro = aux
        
        ultima=1
        #Aciona a rotação do segundo cilindro
        if(trigger==i):
            aux2 = rotacao_direita(seg_cilindro)
            seg_cilindro = aux2
            trigger = trigger+25
            ultima=2
        
        #Aciona a rotação do terceiro cilindro
        if(i==trigger3):
            aux3 = rotacao_direita(ter_cilindro)
            ter_cilindro = aux3
            trigger3 = trigger3+675
            ultima=3
        
        print('1',prim_cilindro)
        print('2',seg_cilindro)
        print('3',ter_cilindro,'\n')
        
        cifrado.append(saida)
    

    #Escrever no arquivo cifrado
    with open('cifrado.txt', 'w') as f:
        for item in cifrado:
            f.write('%s' % item)
    
    print("Texto cifrado em cifrado.txt!\n")

    #Se o ultimo cilindro rotacionado for o segundo, rotaciona de volta
    decifrado =[]
    if(ultima==2):
        aux2 = rotacao_esquerda(seg_cilindro)
        seg_cilindro = aux2
    
    #Se o ultimo cilindro rotacionado for o terceiro, rotaciona de volta
    if(ultima==3):
        aux3 = rotacao_esquerda(ter_cilindro)
        ter_cilindro = aux3
        aux2 = rotacao_esquerda(seg_cilindro)
        seg_cilindro = aux2
    
    #Rotacionar uma vez de volta o primeiro cilindro para pegar o estado anterior dele
    aux = rotacao_esquerda(prim_cilindro)
    prim_cilindro = aux

    trigger2 = trigger - 24 #Setar o trigger do segundo cilindro
    trigger3 = trigger3 - 674 #Setar o trigger do terceiro cilindro
    
    input("Aperte enter para decifrar...")
    print("Decifrando...")
    """Decifrar o cifrado - Começando da ultima letra"""
    for i in range(len(cifrado)-1,-1,-1):
        d = cifrado[i]
        #Consertar uma rotação a mais
        if(i==0):
            aux2 = rotacao_direita(seg_cilindro)
            seg_cilindro = aux2
            aux3 = rotacao_direita(ter_cilindro)
            ter_cilindro = aux3

        saida = decript(prim_cilindro,seg_cilindro,ter_cilindro,d,alfabeto)
        aux = rotacao_esquerda(prim_cilindro)
        
        #Toda vez que atingir o trigger, rotaciona o segundo cilindro
        if(trigger2==i):
            aux2 = rotacao_esquerda(seg_cilindro)
            seg_cilindro = aux2
            trigger2 = trigger2-25
        
        if(trigger3==i):
            aux3 = rotacao_esquerda(ter_cilindro)
            ter_cilindro = aux3
            trigger3 = trigger3-675

        prim_cilindro = aux
        decifrado.append(saida)

    #Reverter a lista pois foi decifrado da esquerda para direita
    decifrado.reverse()
    with open('decifrado.txt', 'w') as f:
        for item in decifrado:
            f.write('%s' % item)
    
    print("Decifrado em decifrado.txt!\n")

main()
