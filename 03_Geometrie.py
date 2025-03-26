import math

class Point:
    def __init__(self, E, N, r=0):
        self.E = E
        self.N = N
        self.radius = r


class Figur():
    def __init__(self, points=[], radius=0):
        self.points = points
        self.radius = radius
        self.name = "Figur"
        self.umfang = self.berechneUmfang()

    def berechneUmfang(self):
        if self.radius > 0:
            return 2 * math.pi * self.radius

        umfang = 0
        for i in range(len(self.points)):
            p1 = self.points[i]
            p2 = self.points[(i + 1) % len(self.points)]
            umfang += math.dist((p1.E, p1.N), (p2.E, p2.N))
        return umfang
    

    def __str__(self):
        if self.radius > 0:
            return f"{self.name}: Mittelpunkt = ({self.points[0].E}, {self.points[0].N}), Radius = {self.radius}, Umfang = {self.umfang}"
        else:
            return f"{self.name}: Umfang = {self.umfang}"
    

class Dreieck(Figur):
    def __init__(self, p1, p2, p3):
        super().__init__([p1, p2, p3])
        self.name = "Dreieck"

    
class Rechteck(Figur):
    def __init__(self, p1, p2, p3, p4):
        super().__init__([p1, p2, p3, p4])
        self.name = "Rechteck"

class Kreis(Figur):
    def __init__(self, mittelpunkt, r):
        super().__init__([mittelpunkt], radius = r)
        self.name = "Kreis"

class Polygon(Figur):
    def __init__(self, *points):
        super().__init__(points)
        self.name = "Polygon"


p1 = Point(0, 0)
p2 = Point(3, 0)
p3 = Point(3, 4)

d1 = Dreieck(p1, p2, p3)
print(d1)

p4 = Point(0, 4)
r1 = Rechteck(p1, p2, p3, p4)
print(r1)

k1 = Kreis(p1, 5)
print(k1)

p5 = Point(1, 1)
p6 = Point(4, 1)
p7 = Point(4, 5)
p8 = Point(1, 5)

poly = Polygon(p1, p2, p3, p4, p5, p6, p7, p8)
print(poly)