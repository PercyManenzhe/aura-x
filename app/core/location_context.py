class LocationContext:
    def __init__(self, province: str = "", municipality: str = "", ward: str = "", area_type: str = ""):
        self.province = province
        self.municipality = municipality
        self.ward = ward
        self.area_type = area_type