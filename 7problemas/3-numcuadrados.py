import math

def cuadrados(n):
    for i in range (1,n+1,1):
        print(i) if not(math.sqrt(i)%1) else (i==i) #resolucion usando la libreria math
        print(i) if not((i**(1/2.0))%1) else (i==i) #resolucion sin usar libreria
        
cuadrados(int(input("\nIntroduzca un numero\n")))