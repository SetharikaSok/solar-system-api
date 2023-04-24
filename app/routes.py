from flask import Blueprint, jsonify

class Planet():
    def __init__ (self, id, name, description, color):
        self.id = id
        self.name = name
        self.description = description
        self.color = color


planets = [
    Planet(1, "Mars", "Similar to Earth", "Copper"),
    Planet(2, "Neptune", "Farthest planet in solar system", "Blue"),
    Planet(3, "Earth", "Where life is known to exist", "Blue-Green"),
    ]

planet_bp = Blueprint("planets", __name__, url_prefix="/planets")
@planet_bp.route("", methods = ["GET"])

def handle_planet():
    planet_response= []
    for planet in planets:
        planet_response.append({
            "id":planet.id,
            "name":planet.name,
            "description":planet.description,
            "color":planet.color
            
        })

    return jsonify(planet_response)

