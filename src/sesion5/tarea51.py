class Punto():
    def __init__(self, p2x, p1x, p2y, p1y):
        self.p2x = p2x
        self.p1x = p1x
        self.p2y = p2y
        self.p1y = p1y
    def distancia(self):
        return self.p2x-self.p1x*2+self.p2y-self.p1y*2
def  principal():
     obj = Punto(10,0,0,0)
     print ('La Distancia entre los puntos es: ', obj.distancia())
if __name__ == '__main__':
     principal()
