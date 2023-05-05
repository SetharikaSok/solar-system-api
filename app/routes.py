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

def validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    except:
        abort(make_response({"message": f"{model_id} invalid"}, 400))
    model = cls.query.get(model_id)
    if not model:
        abort(make_response({"message": f"{cls.__name__} {model_id} not found"}, 404))
    return model

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

def create_planet():
    request_body = request.get_json()
    new_planet = Planet.from_dict(request_body)

    db.session.add(new_planet)
    db.session.commit()

    return jsonify(f"planet {new_planet.name} succesfully created!"), 201

@planet_bp.route("", methods=['GET'])
def read_all_planets():
    name_query = request.args.get("name")
    color_query = request.args.get("color")

    if name_query:
        planets = Planet.query.filter_by(name = name_query)

    elif color_query:
        planets = Planet.query.filter_by(color = color_query)

    else:
        planets = Planet.query.all()

    planets_response = []
    for planet in planets:
        planets_response.append(planet.to_dict())
    return jsonify(planets_response), 200

#define a route for getting a single crystal
#GET /planet/planet_id

@planet_bp.route("/<planet_id>", methods=["GET"])
def read_single_planet(planet_id):
    planet = validate_model(Planet, planet_id)

    return planet.to_dict(),200

@planet_bp.route("/<planet_id>", methods=["PUT"])
def update_planet(planet_id):
    planet = validate_model(Planet, planet_id)

    request_body = request.get_json()
    
    planet.name = request_body["name"]
    planet.color = request_body["color"]
    planet.description = request_body["description"] 

    db.session.commit()

    return planet.to_dict(), 200

@planet_bp.route("/<planet_id>", methods=["DELETE"])
def delete_planet(planet_id):
    planet = validate_model(Planet, planet_id)

    db.session.delete(planet)
    db.session.commit()

    return make_response(f"Planet #{planet_id} successfully deleted!")

