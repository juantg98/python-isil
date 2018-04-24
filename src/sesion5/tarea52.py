from tarea51 import Punto
class Triangulo(Punto):

	def perimetro(self):
		return (self.p2x+self.p1x+self.p2y+self.p1y)

obj = Triangulo(10,0,0,0)
print ('La Suma de la Distancia entre los puntos es: ', obj.perimetro())