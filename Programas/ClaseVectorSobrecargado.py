class Vector:
	def __init__(self, val):
		self.valores = val
		
	def __mul__(self, a):
		resul = [None]*len(self.valores)
		for i in range(len(self.valores)):
			resul[i] = a*self.valores[i]
		return resul
		
vec1 = Vector([1,4,5,6,7])

print(vec1*5)
