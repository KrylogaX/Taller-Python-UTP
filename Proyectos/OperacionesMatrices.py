class Matriz:
    """Clase Matriz que contiene sus valores dimensiones y almacena sus transformaciones"""
    
    def __init__(self):
        """Inicializa la clase matriz.valores
        
        """
        self.filas = 0
        self.columnas = 0
        self.valores = []
        self.traspuesta = []
        self.multi = []
        self.inversa = []

    def setColumnas(self,n):
        """Recibe y asigna el numero de columnas
        
        """
        self.columnas = n

    def setFilas(self, n):
        """Recibe y asigna el numero de filas
        
        """
        self.filas = n

    def getColumnas(self):
        """Retorna el numero de columnas
        
        """
        return self.columnas

    def getFilas(self):
        """Retorna el numero de filas
        
        """
        return self.filas

    def setDimensiones(self):
        """Iniciliza la lista de valores de la matriz.valores, en 0
        
        """
        for i in range(self.filas):
            self.valores.append([0]*(self.columnas))

    def setValor(self, valor, fila, columna):
        """Recibe el valor y posicion de un elemento y lo asigna en la matriz.valores valores
        
        """
        self.valores[fila][columna] = valor

    def imprimir(self):
        """Imprime la matriz
        
        """
        print("\n Imprimiendo la matriz\n")
        for i in range(0,self.filas):
            for j in range(0,self.columnas):
                if j == self.columnas - 1:
                    print(self.valores[i][j],'\n')
                else:
                    print(self.valores[i][j],"   ", end ='')

    def transposicionar(self):
        """Trasposiciona la matriz y la almacena en la traspuesta
        
        """
        self.traspuesta = [None]*len(self.valores[0])
        for i in range(self.columnas):
            self.traspuesta[i] = [None]*len(self.valores)
            for j in range(self.filas):
                self.traspuesta[i][j] = self.valores[j][i]

    def imprimirTraspuesta(self):
        """Imprime la traspuesta
        
        """
        print("\n Imprimiendo la traspuesta\n")
        for i in range(0,self.columnas):
            for j in range(0,self.filas):
                if j == self.filas - 1:
                    print(self.traspuesta[i][j],'\n')
                else:
                    print(self.traspuesta[i][j],"   ", end ='')
    
    def __mul__(self, matriz):
        """Multiplica la matriz 1 y 2 usando sobrecarga de operadores
        
        """
        if self.columnas != matriz.filas:
            print("Dimensiones incorrectas, No se pueden multiplicar")
            return

        self.multi = [[0 for row in range(matriz.columnas)] for col in range(self.filas)]
        print(self.multi)

        for i in range(self.filas):
            for j in range(matriz.columnas):
                for k in range(self.columnas):
                    self.multi[i][j] += self.valores[i][k] * matriz.valores[k][j]

    def imprimirMulti(self):
        """Imprime el resultado de la multiplicacion

        """
        print("\n Imprimiendo la multiplicacion\n")
        for i in range(0,len(self.multi)):
            for j in range(0,len(self.multi[0])):
                if j == len(self.multi[0]) - 1:
                    print(self.multi[i][j],'\n')
                else:
                    print(self.multi[i][j],"   ", end ='')
    
    def invertir(self):
        pass

    def imprimirInversa(self):
        """Imprime la matriz inversa
        
        """
        print("\n Imprimiendo la matriz inversa\n")
        for i in range(0,self.filas):
            for j in range(0,self.columnas):
                if j == self.columnas - 1:
                    print(self.inversa[i][j],'\n')
                else:
                    print(self.inversa[i][j],"   ", end ='')

menu = " "
matriz1 = Matriz()
matriz2 = Matriz()

while menu:
    menu = int(input("\n Qué desea hacer? \n 1. Multiplicacion de matrices \n 2. Transposicion de una matriz \n 3. Inversion de una matriz \n 0. Salir \n\n "))
    if menu == 1:#Multiplicacion de matrices
        matriz1.__init__()
        matriz2.__init__()

        matriz1.setColumnas(int(input("\n Introduzca el numero de columnas de la matriz 1 \n")))
        matriz1.setFilas(int(input("\n Introduzca el numero de filas de la matriz 1 \n")))
        matriz1.setDimensiones()

        for i in range(0,matriz1.filas):
            for j in range(0,matriz1.columnas):
                print('Ingrese el valor de la posicion = [',i,'][',j,'] de la matriz 1\n')
                matriz1.setValor(int(input(),),i,j)

        matriz2.setColumnas(int(input("\n Introduzca el numero de columnas de la matriz 2\n")))
        matriz2.setFilas(int(input("\n Introduzca el numero de filas de la matriz 2\n")))
        matriz2.setDimensiones()

        for i in range(0,matriz2.filas):
            for j in range(0,matriz2.columnas):
                print('Ingrese el valor de la posicion = [',i,'][',j,'] de la matriz 2\n')
                matriz2.setValor(int(input(),),i,j)

        matriz1 * matriz2

        if matriz1.columnas == matriz2.filas:
            matriz1.imprimir()
            matriz2.imprimir()
            matriz1.imprimirMulti()
        
        input('Presione enter para continuar')
        
    elif menu == 2:#Matriz Traspuesta
        matriz1.__init__()
        matriz1.setColumnas(int(input("\n Introduzca el numero de columnas \n")))
        matriz1.setFilas(int(input("\n Introduzca el numero de filas \n")))
        matriz1.setDimensiones()

        for i in range(0,matriz1.filas):
            for j in range(0,matriz1.columnas):
                print('Ingrese el valor de la posicion = [',i,'][',j,'] \n')
                matriz1.setValor(int(input(),),i,j)
        matriz1.imprimir()
        matriz1.transposicionar()
        matriz1.imprimirTraspuesta()
        
        input('Presione enter para continuar')

    elif menu == 3:#Matriz Inversa
        matriz1.__init__()
        matriz1.setColumnas(int(input("\n Introduzca el numero de columnas \n")))
        matriz1.setFilas(int(input("\n Introduzca el numero de filas \n")))
        matriz1.setDimensiones()

        for i in range(0,matriz1.filas):
            for j in range(0,matriz1.columnas):
                print('Ingrese el valor de la posicion = [',i,'][',j,'] \n')
                matriz1.setValor(int(input(),),i,j)

        matriz1.imprimir()
        matriz1.invertir()
        #matriz1.imprimirInversa()
        
        input('Presione enter para continuar')

    elif menu==0:
        input("\nAdios\n")
