import json

#Ler arquivos da chave pública
with open('pu.txt') as f:
    public_key = json.load(f) #Armazena em uma lista [e,n]

claro = open("claro.txt").read() #Ler o texto claro
letras = [str(d) for d in claro] #Separa o texto cada caractere e coloca em uma lista

pb = format(public_key[0], '08b') #Chave pública em 8 bits

#Converte cada letra para seu valor numérico correspondente
numeros = []
for i in range(len(letras)):
    bin = ord(letras[i]) 
    numeros.append(bin)

#print(numeros)

#Pega a chave pública para cifrar
n = public_key[1]
e = public_key[0]
cifrado = [] #Cria uma lista de valores cifrados

#Cifra cada letra do texto através da aritmética modular
bits1 = [] #Lista de bits que contém valor 1 na chave
for i in range(8):
    if int(pb[i]) == 1:
        expoente = 7-i
        valor = pow(2,expoente) #Eleva ao quadrado na posição do bit 0 até 7
        bits1.append(valor)

#Aplica a aritmética modular para cada bit 1 da chave
finalcifrado = []
for x in range(len(numeros)):
    c=1
    for y in range(len(bits1)):
        c = (c * pow(numeros[x], bits1[y])) % n
    cifrado.append(format(c, '08b'))
    finalcifrado.append(c)

print("Cifrado: ")
print(cifrado)
print(finalcifrado)

#Escreve no texto cifrado cada valor em cada linha diferente
with open("c.txt", "w") as f:
    for item in cifrado:
        f.write('%s' %item)


print("Texto cifrado armazenado em c.txt!")

