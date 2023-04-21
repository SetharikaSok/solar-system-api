from flask import Blueprint

class Planet():
    def __init__ (self, id, name, description, color):
        self.id = id
        self.name = name
        self.description = description
        self.color = color


planets = [
    Plant(1, "Mars", "Similar to Earth", "Copper"),
    Plant(2, "Neptune", "Farthest planet in solar system", "Blue"),
    Plant(3, "Earth", "Where life is known to exist", "Blue-Green"),
    ]

planet_bp = Blueprint("planets", __name__, url_prefix="/planets")