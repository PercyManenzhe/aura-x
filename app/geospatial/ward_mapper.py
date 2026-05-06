

class WardMapper:
    

    def map(self, province):
        return {
            "ward": province.location.ward,
            "municipality": province.location.municipality,
            "coordinates": self.get_coordinates(province.location.ward)
        }

    def get_coordinates(self, ward):
        """
        Placeholder — later connect real GIS data
        """
        return {
            "lat": -25.0,
            "lng": 30.0
        }