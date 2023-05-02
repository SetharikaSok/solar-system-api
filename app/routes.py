from flask import Blueprint, jsonify, abort, make_response, request
from app import db
from app.models.planet import Planet




# class Planet():
#     def __init__ (self, id, name, description, color):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.color = color


# planets = [
#     Planet(1, "Mars", "Similar to Earth", "Copper"),
#     Planet(2, "Neptune", "Farthest planet in solar system", "Blue"),
#     Planet(3, "Earth", "Where life is known to exist", "Blue-Green"),
#     ]

# def validate_planet(planet_id):
#     try:
#         planet_id = int(planet_id)
#     except:
#         abort(make_response({"message": f"planet {planet_id} invalid"}, 400))

#     for planet in planets:
#         if planet.id == planet_id:
#             return planet
#     abort(make_response({"message": f"planet {planet_id} not found"}, 404))

planet_bp = Blueprint("planets", __name__, url_prefix="/planets")
# @planet_bp.route("", methods = ["GET"])

# def handle_planets():

#     planet_response= []

#     for planet in planets:
#         planet_response.append({
#             "id":planet.id,
#             "name":planet.name,
#             "description":planet.description,
#             "color":planet.color
            
#         })

#     return jsonify(planet_response)

# @planet_bp.route("/<planet_id>", methods = ["GET"])

# def handle_planet(planet_id):

#     planet= validate_planet(planet_id)
    
#     return{
#             "id":planet.id,
#             "name":planet.name,
#             "description":planet.description,
#             "color":planet.color
            
#         }

    

@planet_bp.route("",methods = ["POST"])

#definbe a route for creating a planet resource

def handle_planets():
    request_body = request.get_json()
    new_planet = Planet (
            name = request_body["name"],
            color = request_body["color"],
            description = request_body["description"] 


    )

    db.session.add(new_planet)
    db .session.commit()

    return make_response(f"planet {new_planet.name} succesfully created", 201)

@planet_bp.route("", methods=['GET'])
def read_all_planets():
    planets_response = []
    planets = Planet.query.all()
    for planet in planets:
        planets_response.append({
            "id": planet.id,
            "name": planet.name,
            "color": planet.color,
            "description": planet.description
        })
    return jsonify(planets_response), 200

#define a route for getting a single crystal
#GET /planet/planet_id

@planet_bp.route("/<planet_id>", methods=["GET"])
def read_single_planet(planet_id):
    planet = Planet.query.get(planet_id)

    return {
            "id": planet.id,
            "name": planet.name,
            "color": planet.color,
            "description": planet.description
        },200
