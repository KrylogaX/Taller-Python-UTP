class NumBinario:
	def __init__(self,num):
		self.numero = list(num)
		self.numeroT = num
		
		if check():
			self.decimal = int(num,2)
		
	def check(self):
		for i in self.numero: 
			if i!=1 or i!=0:
				return False
		return True

		
	def __add__(self, num2):
		resul = []
		acarreo = []
		cant1 = len(self.numero)
		cant2 = len(num2.numero)
		largo = cant1 if cant1>cant2 else cant2
		
		if can1 > cant2:
			resul = [0]*(cant1+1)
			acarreo = [0]*(cant1+1)
			
		else:
			resul = [0]*(cant2+1)
			acarreo = [0]*(cant2+1)
		
		for i in range(largo):
			if self.numero[i] ==0 or num2.numero[i] ==0:
				if self.numero[i] ==1 or num2.numero[i] ==1:
					resul[i]=1
				else:
					resul[i]=0
			else:
				resul[i]=0
				acarreo[i+1]=1
	
	def __sub__(self, a):
		return bin(int(self.numero,2)-int(a.numero,2))
		
	def __mul__(self, a):
		return bin(int(self.numero,2)*int(a.numero,2))
		
	def __truediv__(self, a):
		return bin(int(self.numero,2)/int(a.numero,2))
		
	def __repr__(self):
		return 'El valor del numero binario es: %s y en decimal: %s ' % (self.numeroT,self.decimal)
		
	
numerobinario1 = NumBinario(input("\nIntroduzca un numero binario\n"))
numerobinario2 = NumBinario(input("Introduzca otro numero binario\n"))

if(not(numerobinario1.check() and numerobinario2.check())):
	print(numerobinario1.numero,' No es un numero entero')

print(numerobinario1.numero)
print(numerobinario2.numero)

print(numerobinario1,numerobinario2)


#print(numerobinario1+numerobinario2)
#print(numerobinario1-numerobinario2)
#print(numerobinario1*numerobinario2)
#print(numerobinario1/numerobinario2)

