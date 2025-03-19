class Vector3:
    def __init__(self, x = 0.0, y = 0.0, z = 0.0):
        self._x = x
        self._y = y
        self._z = z


    def setX(self, x):
        self._x = x

    def getX(self):
        return self._x

    def setY(self, y):
        self._x = y

    def getY(self):
        return self._y
    
    def setZ(self, z):
        self._z = z

    def getZ(self):
        return self._z
    
    
    def __str__(self):
        return f"x: {self.x} y: {self.y} z: {self.z}"
    

    def __add__(self, addVector):
        return Vector3(self.x + addVector.x, self.y + addVector.y, self.z + addVector.z)
    
    def __sub__(self, subVector):
        return Vector3(self.x - subVector.x, self.y - subVector.y, self.z - subVector.z)

    def __mul__(self, multiplicator):
        return Vector3(self.x * multiplicator, self.y * multiplicator, self.z * multiplicator)
    

    def dot(self, second):
        return (self.x*second.x + self.y*second.y + self.z*second.z)

    def cross(self, second):
        return Vector3((self.y*second.z - self.z*second.y), (self.z*second.x - self.x*second.z), (self.x*second.y - self.y*second.x))
    
    def normalize(self):
        len = (self.x**2 + self.y**2 + self.z**2)**0.5
        return Vector3(self.x/len, self.y/len, self.z/len)

    
    x = property(getX, setX)
    y = property(getY, setY)
    z = property(getZ, setZ)


a = Vector3(3,4,2)
b = Vector3(2,1,0)


print(f"Zeichenkette: {str(a)}")
print(f"Addition: {a + b}")
print(f"Subtraktion: {a - b}")
print(f"Multiplikation: {a * 3}")
print(f"Skalarprodukt:  {a.dot(b)}")
print(f"Kreuzprodukt:   {a.cross(b)}")
print(f"Normierung:   {a.normalize()}")


