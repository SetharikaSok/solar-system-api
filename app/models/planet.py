from app import db

class Planet(db.Model):
    id = db.Column(db.Integer,primary_key = True, autoincrement = True)
    name = db.Column(db.String)
    color = db.Column(db.String)
    description = db.Column(db.String)

    @classmethod
    def from_dict(cls, planet_data):
        new_planet = Planet(
            name = planet_data['name'],
            color = planet_data['color'],
            description = planet_data['description']
        )
        return new_planet
        
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "color": self.color,
            "description": self.description
        }

