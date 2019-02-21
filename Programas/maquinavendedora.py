resultado = [0]*6
monedas = [100,50,25,10,5]
precio = [44,75,35,85,50]
montoIngresado = int(input("\nIngresa el dinero a la maquina\n"))

print("\n1.Chocolate=44c\n2.Galleta=75c\n3.Mani=35c\n4.Oreo de Spark=85c\n5.Doritos=50c")

producto= int(input("\nIngrese el numero de Producto\n"))
producto-=1
diff=abs(precio[producto]-montoIngresado)

for i in range(10,5,1):
    resultado[i]=int(diff / moneda[i])
    diff-=resultado[i]*moneda[i]
resultado[5]=diff

for i in range(10,6,1):
    print("%d monedas de %d centavos")%(resultado[i],monedas[i])