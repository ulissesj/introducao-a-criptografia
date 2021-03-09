p = input("Informe o p(número primo): ")
q = input("Informe o q(número primo): ")
e = input("Informe o e(primo relativo menor que phi): ")

n = (int(p) * int(q)) #Cálculo de n
phi = ((int(p)-1) * (int(q)-1)) #Cálculo de phi

#Calcular d pelo método iterativo
for y in range(1,phi):
    d = (1+(y*phi))/int(e)
    check_int = d.is_integer() #Retorna True se d for um inteiro
    if (check_int == True): 
        break

e = int(e) #Chave pública
d = int(d) #Chave privada

public_key = [e,n]
#Armazena no arquivo a chave pública
pu = open("pu.txt", 'w')
pu.write(str(public_key))
print("Chave pública armazenada em pu.txt")

private_key = [d,n]
#Armazena no arquivo a chave privada
pr = open("pr.txt", 'w')
pr.write(str(private_key))
print("Chave privada armazenada em pu.txt")