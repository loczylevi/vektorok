
class Vektor:
    def __init__(self,x,y,z=0):
        self.x = x
        self.y = y
        self.z = z
    def print(self):
        print(self.x,self.y)
    def hossz(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5
    def __add__(self, b):
        return Vektor(self.x + b.x, self.y + b.y, self.z + b.z)
    def __sub__(self, b):
        return Vektor(self.x - b.x, self.y - b.y, self.z - b.z)
    #def __mul__(self, b):
        #if type(self) == type(int()) or type(self) == type(float()):
            #return Vektor(b * self.x, b * self.y, b * self.z)
        

