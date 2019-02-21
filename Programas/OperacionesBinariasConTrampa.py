class NumBinario:
	def __init__(self,num):
		self.numero = num
		self.decimal = num
		self.numcadena = list(num)
	
	def converDecimal(self):
		self.decimal = int(self.numero,2)
		
	def check(self):
		for i in range(0,len(self.numcadena)-1): 
			if self.numcadena[i]!='0' and self.numcadena[i]!='1':
				return False
					
		return True
			
	def __add__(self, a):
		return bin(int(self.numero,2)+int(a.numero,2))
	
	def __sub__(self, a):
		return bin(int(self.numero,2)-int(a.numero,2))
		
	def __mul__(self, a):
		return bin(int(self.numero,2)*int(a.numero,2))
		
	def __truediv__(self, a):
		return bin(int(self.numero,2)//int(a.numero,2))
	
	def __repr__(self):
		return 'El valor del numero binario es: %s y en decimal: %s ' % (self.numero,self.decimal)
		
		
numerobinario1 = NumBinario(input("Introduzca un numero binario\n"))
numerobinario2 = NumBinario(input("Introduzca otro numero binario\n"))

if (numerobinario1.check() and numerobinario2.check()):
	
	numerobinario1.converDecimal()
	numerobinario2.converDecimal()
	
	if (numerobinario2.decimal == 0):
		print("No se puede dividir entre 0")
	else:
		print(numerobinario1+numerobinario2)
		print(numerobinario1-numerobinario2)
		print(numerobinario1*numerobinario2)
		print(numerobinario1/numerobinario2)
		print(numerobinario1)
		print(numerobinario2)
else:
	print("Uno de estos numeros no es binario")
