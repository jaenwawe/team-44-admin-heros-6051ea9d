class Position:
    MIN_LAT = 0
    MIN_LON = 0
    MAX_LAT = 9
    MAX_LON = 9
    lat = -1
    lon = -1

    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

    def isValid(self):
        return self.lat >= self.MIN_LAT and self.lat <= self.MAX_LAT and self.lon >= self.MIN_LON and self.lon <= self.MAX_LON