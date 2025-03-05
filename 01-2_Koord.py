class WGS84Coord():
    def __init__(self, long = 0, lat = 0):
        self._longitude = long
        self._latitude = lat
        self.coord()

    def getlat(self):
        return self._latitude
    
    def setlat(self, lati):
        self._latitude = lati
        self.coord()

    def getlong(self):
        return self._longitude
    
    def setlong(self, longi):
        self._longitude = longi
        self.coord()


    def coord(self):

        while self._latitude > 90 or self._latitude < -90:
            
            if  self._latitude > 90:
                self._latitude = 180 - self._latitude
                self._longitude +=  180

            elif self._latitude < -90:
                self._latitude = - 180 - self._latitude
                self._longitude +=  180


        while self._longitude > 180 or self._longitude < -180:
            
            if  self._longitude > 180:
                self._longitude -= 360

            elif self._longitude < -180:
                self._longitude += 360

    def ausgabe(self):
        print (f"Längengrad: {self._longitude}, Breitengrad: {self._latitude}")


    longitude = property(getlong, setlong)
    latitude = property(getlat, setlat)

a = WGS84Coord()

a.longitude = 0        #reihenfolge unbedingt beachten (zuerst long, dann lat)
a.latitude = 269

a.ausgabe()

print("Latitude:", a.latitude)
print("Longitude:", a.longitude)

