
class Vector3():
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def len(self):
        return (((self.x**2)+(self.y**2)+(self.z**2))**0.5)
    
    


a = Vector3(5,8,3)
print (a.len())

