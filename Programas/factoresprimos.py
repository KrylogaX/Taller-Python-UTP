#Kendall Kant
def revisar_factores (num):
    lista_factores = []
    for i in range(1,num+1):
        if (num%i==0):lista_factores.append(i)
    return lista_factores
def revisar_primos (lista):
    primos = []
    for i in range(0,len(lista)):
        cont = 0
        for j in range (1,lista[i]+1):
            if(lista[i]%j==0): cont+=1
        if (cont==2): primos.append(lista[i])
    return primos
factores = revisar_factores(int(input("\nIntroduzca un numero entero\n")))
primos = revisar_primos(factores)
print("\nLos factores son: ",factores,"\nde esos factores los primos son",primos,"\n")