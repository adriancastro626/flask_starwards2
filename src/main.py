"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Planet, People, Vehicle
import json
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Setup the Flask-JWT-Extended extension
app.config["JWT_SECRET_KEY"] = os.environ.get('JWT_SECRET') # Change this!
jwt = JWTManager(app)

# TOKEN

# Create a route to authenticate your users and return JWTs. The
# create_access_token() function is used to actually generate the JWT.
@app.route("/token", methods=["POST"])
def create_token():    
    email = request.json.get("email", None)
    password = request.json.get("password", None)
    if email != "test" or password != "test":
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=email)
    return jsonify(access_token=access_token)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

# START CRUD USER

@app.route('/user', methods=['GET'])
def handle_user():

    users = User.query.all()
    all_users = list(map(lambda x: x.serialize(), users))

    return jsonify(all_users), 200

@app.route('/user/<int:id>', methods=['GET'])
def getSingleUser(id):
    user = User.query.get(id)
    return jsonify(user.serialize()), 200

@app.route('/user', methods=['POST'])
def create_user():

    request_body_user = request.get_json()

    newUser = User(name=request_body_user["name"], lastname=request_body_user["lastname"], username=request_body_user["username"], email=request_body_user["email"], password=request_body_user["password"])
    db.session.add(newUser)
    db.session.commit()

    return jsonify(request_body_user), 200

@app.route('/user/<int:user_id>', methods=['PUT'])
def edit_user(user_id):

    request_body_user = request.get_json()

    updateUser = User.query.get(user_id)
    if updateUser is None:
        raise APIException('User not found', status_code=404)

    if "name" in request_body_user:
        updateUser.name = request_body_user["name"]
    if "lastname" in request_body_user:
        updateUser.lastname = request_body_user["lastname"]
    if "username" in request_body_user:
        updateUser.username = request_body_user["username"]
    if "email" in request_body_user:
        updateUser.email = request_body_user["email"]
    if "password" in request_body_user:
        updateUser.password = request_body_user["password"]
    db.session.commit()

    return jsonify(request_body_user), 200

@app.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
        
    deleteUser = User.query.get(user_id)
    if deleteUser is None:
        raise APIException('User not found', status_code=404)
    db.session.delete(deleteUser)
    db.session.commit()

    return jsonify("Eliminado"), 200

# START CRUD PLANET

@app.route('/planet', methods=['GET'])  #Mostrar info
def handle_planet():

    planets = Planet.query.all()
    all_planets = list(map(lambda x: x.serialize(), planets))

    return jsonify(all_planets), 200

@app.route('/planet/<int:id>', methods=['GET'])
def getSinglePlanet(id):
    planet = Planet.query.get(id)
    return jsonify(planet.serialize()), 200

@app.route('/planet', methods=['POST']) #Crear nuevo 
def create_planet():

    request_body_planet = request.get_json()

    newPlanet = Planet(planet_name=request_body_planet["planet_name"], population=request_body_planet["population"], terrain=request_body_planet["terrain"])
    db.session.add(newPlanet)
    db.session.commit()

    return jsonify(request_body_planet), 200

@app.route('/planet/<int:planet_id>', methods=['PUT']) #Actualizar 
def edit_planet(planet_id):

    request_body_planet = request.get_json()

    updatePlanet = Planet.query.get(planet_id)
    if updatePlanet is None:
        raise APIException('User not found', status_code=404)

    if "planet_name" in request_body_planet:
        updatePlanet.planet_name = request_body_planet["planet_name"]
    if "population" in request_body_planet:
        updatePlanet.population = request_body_planet["population"]
    if "terrain" in request_body_planet:
        updatePlanet.terrain = request_body_planet["terrain"]    
    db.session.commit()

    return jsonify(request_body_planet), 200

@app.route('/planet/<int:planet_id>', methods=['DELETE']) #Borrar 
def delete_planet(planet_id):
        
    deletePlanet = Planet.query.get(planet_id)
    if deletePlanet is None:
        raise APIException('User not found', status_code=404)
    db.session.delete(deletePlanet)
    db.session.commit()

    return jsonify("Eliminado"), 200

# START CRUD PEOPLE

@app.route('/people', methods=['GET'])  #Mostrar info
def handle_people():

    peoples = People.query.all()
    all_peoples = list(map(lambda x: x.serialize(), peoples))

    return jsonify(all_peoples), 200

@app.route('/people/<int:id>', methods=['GET'])
def getSinglePeople(id):
    people = People.query.get(id)
    return jsonify(people.serialize()), 200

@app.route('/people', methods=['POST']) #Crear nuevo 
def create_people():

    request_body_people = request.get_json()

    newPeople = People(name=request_body_people["name"], last_name=request_body_people["last_name"], power=request_body_people["power"])
    db.session.add(newPeople)
    db.session.commit()

    return jsonify(request_body_people), 200

@app.route('/people/<int:people_id>', methods=['PUT']) #Actualizar 
def edit_people(people_id):

    request_body_people = request.get_json()

    updatePeople = People.query.get(people_id)
    if updatePeople is None:
        raise APIException('User not found', status_code=404)

    if "name" in request_body_people:
        updatePeople.name = request_body_people["name"]
    if "last_name" in request_body_people:
        updatePeople.last_name = request_body_people["last_name"]
    if "power" in request_body_people:
        updatePeople.power = request_body_people["power"]    
    db.session.commit()

    return jsonify(request_body_people), 200

@app.route('/people/<int:people_id>', methods=['DELETE']) #Borrar 
def delete_people(people_id):
        
    deletePeople = People.query.get(people_id)
    if deletePeople is None:
        raise APIException('User not found', status_code=404)
    db.session.delete(deletePeople)
    db.session.commit()

    return jsonify("Eliminado"), 200


# START CRUD VEHICLE

@app.route('/vehicle', methods=['GET'])  #Mostrar info
def handle_vehicle():

    vehicles = Vehicle.query.all()
    all_vehicles = list(map(lambda x: x.serialize(), vehicles))

    return jsonify(all_vehicles), 200

@app.route('/vehicle/<int:id>', methods=['GET'])
def getSingleVehicle(id):
    vehicle = Vehicle.query.get(id)
    return jsonify(vehicle.serialize()), 200

@app.route('/vehicle', methods=['POST']) #Crear nuevo 
def create_vehicle():

    request_body_vehicle = request.get_json()

    newVehicle = Vehicle(brand=request_body_vehicle["brand"], capacity=request_body_vehicle["capacity"], color=request_body_vehicle["color"])
    db.session.add(newVehicle)
    db.session.commit()

    return jsonify(request_body_vehicle), 200

@app.route('/vehicle/<int:vehicle_id>', methods=['PUT']) #Actualizar 
def edit_vehicle(vehicle_id):

    request_body_vehicle = request.get_json()

    updateVehicle = Vehicle.query.get(vehicle_id)
    if updateVehicle is None:
        raise APIException('User not found', status_code=404)

    if "name" in request_body_vehicle:
        updateVehicle.name = request_body_vehicle["name"]
    if "last_name" in request_body_vehicle:
        updateVehicle.last_name = request_body_vehicle["last_name"]
    if "power" in request_body_vehicle:
        updateVehicle.power = request_body_vehicle["power"]    
    db.session.commit()

    return jsonify(request_body_vehicle), 200

@app.route('/vehicle/<int:vehicle_id>', methods=['DELETE']) #Borrar 
def delete_vehicle(vehicle_id):
        
    deleteVehicle = Vehicle.query.get(vehicle)
    if deleteVehicle is None:
        raise APIException('User not found', status_code=404)
    db.session.delete(deleteVehicles)
    db.session.commit()

    return jsonify("Eliminado"), 200

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)

