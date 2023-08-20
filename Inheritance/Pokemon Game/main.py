class Pokemon:
    def __init__(self, name, level):
        self.name = name
        self.level = level
    
    def display_info(self):
        return f"Name: {self.name}, Level: {self.level}"

class FireType(Pokemon):
    def __init__(self, name, level):
        super().__init__(name, level)
        self.type = "Fire"
    
    def display_info(self):
        return f"{super().display_info()}, Type: {self.type}"

class WaterType(Pokemon):
    def __init__(self, name, level):
        super().__init__(name, level)
        self.type = "Water"
    
    def display_info(self):
        return f"{super().display_info()}, Type: {self.type}"

class GrassType(Pokemon):
    def __init__(self, name, level):
        super().__init__(name, level)
        self.type = "Grass"
    
    def display_info(self):
        return f"{super().display_info()}, Type: {self.type}"

charmander = FireType("Charmander", 5)
squirtle = WaterType("Squirtle", 5)
bulbasaur = GrassType("Bulbasaur", 5)

print(charmander.display_info())
print(squirtle.display_info())
print(bulbasaur.display_info())
