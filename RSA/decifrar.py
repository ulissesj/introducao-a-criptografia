import json

#Ler arquivos da chave privada
with open('pr.txt') as f:
    private_key = json.load(f) #Armazena em uma lista [d,n]

pv = format(private_key[0], '08b') #Chave privada em 8 bits

#Lê o arquivo e coloca numa string
with open('c.txt','r') as file:
    cifradobits = file.read()

bitsarray = [(cifradobits[i:i+8]) for i in range(0, len(cifradobits), 8)] #Separa cada 8 bits

#Converte os binários para inteiro
cifrado = []
for b in range(len(bitsarray)):
    cifrado.append(int(bitsarray[b], 2))

d = private_key[0] #Chave privada
n = private_key[1] 
decifrado = [] #Texto decifrado

#Decifra cada letra do texto através da aritmética modular
bits1 = [] #Lista de bits que contém valor 1 na chave
for i in range(8):
    if int(pv[i]) == 1:
        expoente = 7-i
        valor = pow(2,expoente) #Eleva ao quadrado na posição do bit 0 até 7
        bits1.append(valor)

#Aplica a aritmética modular para cada bit 1 da chave
for x in range(len(cifrado)):
    c=1
    for y in range(len(bits1)):
        c = (c * pow(int(cifrado[x]), bits1[y])) % n
    decifrado.append(chr(c)) #Converte para o caractere correspondente


#Escreve no arquivo d.txt
with open("d.txt", "w") as f:
    for item in decifrado:
        f.write('%s' %item)

print("Texto decifrado armazenado em d.txt!")