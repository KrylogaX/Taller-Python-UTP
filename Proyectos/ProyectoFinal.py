#Programa que cree las clases "Binario", "Octal", "Hexadecimal"
#Con sus respectivas operaciones básicas
#Transformaciones entre sistemas numéricos

#Kendall Kant
#Jose Rivas

#DISCLAIMER: Si me di cuenta de que usando herencia no hubieramos tenido que rehacer las clases 3 veces pero ya habia empezado de esta manera
#Posiblemente en un futuro lo cambiare

class Binario:
    def __init__(self):
        """Construye la funcion y e inicializa todos los atributos en 0
        """
        self.valor = 0
        self.decimal = 0
        self.hexadecimal = 0
        self.octal = 0

    def checkValor(self, n):
        """Obtiene un valor lo convierte en una lista y comprueba que sea binario
            comparado todos sus digitos con la lista de digitos binarios posibles
        """
        listaN = list(n)
        listaBinario = ['0','1']
        for i in range((len(listaN))):
            if listaN[i] in listaBinario:
                pass
            else:
                return False
        return True

    def setValor(self,n):
        """Obtiene un valor cadena, lo convierte a entero base 2, lo transforma a 
            binario y se lo asigna al atributo valor
        """
        self.valor = bin(int(n,2))

    def getValor(self):
        """Retorna el atributo valor
        """
        return self.valor

    def convertDecimal(self):
        """Convierte y asigna el atributo valor binario a decimal
        """
        self.decimal = int(self.valor,2)
    def convertOctal(self):
        """Convierte y asigna el atributo valor binario a octal
        """
        self.octal = oct(int(self.valor,2))
    def convertHexadecimal(self):
        """Convierte y asigna el atributo valor binario a hexadecimal
        """
        self.hexadecimal = hex(int(self.valor,2))
    def convertir(self):
        """Llama a todas las otras funciones de convertir y convierte el numero a todos los otros sistemas
        """
        self.convertHexadecimal()
        self.convertDecimal()
        self.convertOctal()

    def getDecimal(self):
        """Retorna el valor en decimal
        """
        return self.decimal
    def getOctal(self):
        """Retorna el valor en octal
        """
        return self.octal
    def getHexadecimal(self):
        """Retorna el valor en hexadecimal
        """
        return self.hexadecimal

    def __add__(self, a):
        return bin(int(self.valor,2)+int(a.valor,2))
    def __sub__(self, a):
        return bin(int(self.valor,2)-int(a.valor,2))
    def __mul__(self, a):
        return bin(int(self.valor,2)*int(a.valor,2))
    def __truediv__(self, a):
        return bin(int(self.valor,2)//int(a.valor,2))

    def __repr__(self):
        return "El valor del binario %s es \n %s en decimal \n %s en hexadecimal \n %s en octal" % (self.valor,self.decimal,self.hexadecimal,self.octal)

class Octal:
    def __init__(self):
        """Construye la funcion y e inicializa todos los atributos en 0
        """
        self.valor = 0
        self.decimal = 0
        self.hexadecimal = 0
        self.binario = 0

    def checkValor(self, n):
        """Obtiene un valor lo convierte en una lista y comprueba que sea octal
            comparado todos sus digitos con la lista de digitos octales posibles
            
        """
        listaN = list(n)
        listaOctal = ['0','1','2','3','4','5','6','7']
        for i in range((len(listaN))):
            if listaN[i] in listaOctal:
                pass
            else:
                return False
        return True

    def setValor(self,n):
        """Obtiene un valor cadena, lo convierte a entero base 8, lo transforma a 
            octal y se lo asigna al atributo valor
        """
        self.valor = oct(int(n,8))

    def getValor(self):
        """Retorna el atributo valor
        """
        return self.valor

    def convertDecimal(self):
        """Convierte y asigna el atributo valor octal a decimal
        """
        self.decimal = int(self.valor,8)
    def convertHexadecimal(self):
        """Convierte y asigna el atributo valor octal a hexadecimal
        """
        self.hexadecimal = hex(int(self.valor,8))
    def convertBinario(self):
        """Convierte y asigna el atributo valor octal a binario
        """
        self.binario = bin(int(self.valor,8))
    def convertir(self):
        """Llama a todas las otras funciones de convertir y convierte el numero a todos los otros sistemas
        """
        self.convertBinario()
        self.convertDecimal()
        self.convertHexadecimal()

    def getDecimal(self):
        """Retorna el valor en decimal
        """
        return self.decimal
    def getHexadecimal(self):
        """Retorna el valor en hexadecimal
        """
        return self.hexadecimal
    def getBinario(self):
        """Retorna el valor en binario
        """
        return self.binario

    def __add__(self, a):
        return oct(int(self.valor,8)+int(a.valor,8))
    def __sub__(self, a):
        return oct(int(self.valor,8)-int(a.valor,8))
    def __mul__(self, a):
        return oct(int(self.valor,8)*int(a.valor,8))
    def __truediv__(self, a):
        return oct(int(self.valor,8)//int(a.valor,8))

    def __repr__(self):
        return "El valor del octal %s es \n %s en decimal \n %s en binario \n %s en hexadecimal" % (self.valor,self.decimal,self.binario,self.hexadecimal)

class Hexadecimal:
    def __init__(self):
        """Construye la funcion e inicializa todos los atributos en 0

        """
        self.valor = 0
        self.decimal = 0
        self.octal = 0
        self.binario = 0

    def checkValor(self, n):
        """Obtiene un valor lo convierte en una lista y comprueba que sea hexadecimal
            comparado todos sus digitos con la lista de digitos hexadecimales posibles
            
        """
        listaN = list(n)
        listaHexa = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
        for i in range((len(listaN))):
            if listaN[i] in listaHexa:
                pass
            else:
                return False
        return True

    def setValor(self,n):
        """Obtiene un valor cadena, lo convierte a entero base 16, lo transforma a 
            hexadecimal y se lo asigna al atributo valor
        """
        self.valor = hex(int(n,16))

    def getValor(self):
        """Retorna el atributo valor
        """
        return self.valor

    def convertDecimal(self):
        """Convierte y asigna el atributo valor hexadecimal a decimal
        """
        self.decimal = int(self.valor,16)
    def convertOctal(self):
        """Convierte y asigna el atributo valor hexadecimal a octal
        """
        self.octal = oct(int(self.valor,16))
    def convertBinario(self):
        """Convierte y asigna el atributo valor hexadecimal a binario
        """
        self.binario = bin(int(self.valor,16))
    def convertir(self):
        """Llama a todas las otras funciones de convertir y convierte el numero a todos los otros sistemas
        """
        self.convertBinario()
        self.convertDecimal()
        self.convertOctal()

    def getDecimal(self):
        """Retorna el valor en decimal
        """
        return self.decimal
    def getOctal(self):
        """Retorna el valor en octal
        """
        return self.octal
    def getBinario(self):
        """Retorna el valor en binario
        """
        return self.binario

    def __add__(self, a):
        return hex(int(self.valor,16)+int(a.valor,16))
    def __sub__(self, a):
        return hex(int(self.valor,16)-int(a.valor,16))
    def __mul__(self, a):
        return hex(int(self.valor,16)*int(a.valor,16))
    def __truediv__(self, a):
        return hex(int(self.valor,16)//int(a.valor,16))

    def __repr__(self):
        return "El valor del hexadecimal %s es \n %s en decimal \n %s en binario \n %s en octal" % (self.valor,self.decimal,self.binario,self.octal)

menu = " "
while menu:
    menu = int(input("\n Con cual sistema numerico desea trabajar \n 1. Binario \n 2. Octal \n 3. Hexadecimal \n 0. Salir \n\n "))
    if menu == 1: #BINARIO
        menu2 = int(input("\n Que desea hacer \n 1. Conversion a otros sistemas numericos \n 2. Operaciones basicas \n 0. Salir \n\n "))
        if menu2 == 1: #Conversion de BINARIO a otros
            numeroBin = Binario()
            entrada = input("\nIntroduzca un numero Binario\n")
            if numeroBin.checkValor(entrada):
                numeroBin.setValor(entrada)
                numeroBin.convertir()
                print(numeroBin)
                input("Presione enter para continuar\n")
            else:
                print("\nEse numero no es binario\n")
                input("Presione enter para continuar\n")
        elif menu2 == 2: #Operaciones basicas en BINARIO
            numeroBin1 = Binario()
            numeroBin2 = Binario()
            entrada1 = input("\nIntroduzca el primer operando Binario\n")
            entrada2 = input("\nIntroduzca el segundo operando Binario\n")
            if numeroBin1.checkValor(entrada1) and numeroBin2.checkValor(entrada2):
                numeroBin1.setValor(entrada1)
                numeroBin2.setValor(entrada2)
                print(' Suma: ',numeroBin1+numeroBin2,'\n Resta: ',numeroBin1-numeroBin2,'\n Multiplicacion: ',numeroBin1*numeroBin2)
                if numeroBin2.getValor() != hex(0):
                    print(' Division: ',numeroBin1/numeroBin2)
                    input("Presione enter para continuar\n")
                else:
                    print(' Division invalida, el segundo operando es cero')
                    input("Presione enter para continuar\n")
            else:
                print("\nUno de los operandos no es binario\n")
                input("Presione enter para continuar\n")

    elif menu == 2: #OCTAL
        menu2 = int(input("\n Que desea hacer \n 1. Conversion a otros sistemas numericos \n 2. Operaciones basicas \n 0. Salir \n\n "))
        if menu2 == 1: #Conversion de OCTAL a otros
            numeroOct = Octal()
            entrada = input("\nIntroduzca un numero Octal\n")
            if numeroOct.checkValor(entrada):
                numeroOct.setValor(entrada)
                numeroOct.convertir()
                print(numeroOct)
                input("Presione enter para continuar\n")
            else:
                print("\nEse numero no es octal\n")
                input("Presione enter para continuar\n")
        elif menu2 == 2: #Operaciones basicas en OCTAL
            numeroOct1 = Octal()
            numeroOct2 = Octal()
            entrada1 = input("\nIntroduzca el primer operando Octal\n")
            entrada2 = input("\nIntroduzca el segundo operando Octal\n")
            if numeroOct1.checkValor(entrada1) and numeroOct2.checkValor(entrada2):
                numeroOct1.setValor(entrada1)
                numeroOct2.setValor(entrada2)
                print(' Suma: ',numeroOct1+numeroOct2,'\n Resta: ',numeroOct1-numeroOct2,'\n Multiplicacion: ',numeroOct1*numeroOct2)
                if numeroOct2.getValor() != hex(0):
                    print(' Division: ',numeroOct1/numeroOct2)
                    input("Presione enter para continuar\n")
                else:
                    print(' Division invalida, el segundo operando es cero')
                    input("Presione enter para continuar\n")
            else:
                print("\nUno de los operandos no es Octal\n")
                input("Presione enter para continuar\n")

    elif menu == 3: #HEXADECIMAL
        menu2 = int(input("\n Que desea hacer \n 1. Conversion a otros sistemas numericos \n 2. Operaciones basicas \n 0. Salir \n\n "))
        if menu2 == 1: #Conversion de HEXADECIMAL a otros
            numeroHex = Hexadecimal()
            entrada = input("\nIntroduzca un numero Hexadecimal\n")
            if numeroHex.checkValor(entrada):
                numeroHex.setValor(entrada)
                numeroHex.convertir()
                print(numeroHex)
                input("Presione enter para continuar\n")
            else:
                print("\nEse numero no es hexadecimal\n")
                input("Presione enter para continuar\n")
        elif menu2 == 2: #Operaciones basicas en HEXADECIMAL
            numeroHex1 = Hexadecimal()
            numeroHex2 = Hexadecimal()
            entrada1 = input("\nIntroduzca el primer operando Hexadecimal\n")
            entrada2 = input("\nIntroduzca el segundo operando Hexadecimal\n")
            if numeroHex1.checkValor(entrada1) and numeroHex2.checkValor(entrada2):
                numeroHex1.setValor(entrada1)
                numeroHex2.setValor(entrada2)
                print(' Suma: ',numeroHex1+numeroHex2,'\n Resta: ',numeroHex1-numeroHex2,'\n Multiplicacion: ',numeroHex1*numeroHex2)
                if numeroHex2.getValor() != hex(0):
                    print(' Division: ',numeroHex1/numeroHex2)
                    input("Presione enter para continuar\n")
                else:
                    print(' Division invalida, el segundo operando es cero')
                    input("Presione enter para continuar\n")
            else:
                print("\nUno de los operandos no es hexadecimal\n")
                input("Presione enter para continuar\n")
print("\nAdios\n")
input("Presione enter para continuar\n")