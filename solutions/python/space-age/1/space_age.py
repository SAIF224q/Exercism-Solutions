class SpaceAge:
    EARTH_YEAR_SECONDS = 31557600
    
    def __init__(self, seconds):
        self.seconds = seconds
    
    def on_earth(self):
        return round(self.seconds / self.EARTH_YEAR_SECONDS, 2)
    
    def _planet_years(self, orbital_period):
        earth_years = self.seconds / self.EARTH_YEAR_SECONDS
        return round(earth_years / orbital_period, 2)
    
    def on_mercury(self):
        return self._planet_years(0.2408467)
    
    def on_venus(self):
        return self._planet_years(0.61519726)
    
    def on_mars(self):
        return self._planet_years(1.8808158)
    
    def on_jupiter(self):
        return self._planet_years(11.862615)
    
    def on_saturn(self):
        return self._planet_years(29.447498)
    
    def on_uranus(self):
        return self._planet_years(84.016846)
    
    def on_neptune(self):
        return self._planet_years(164.79132)