from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    lastname = db.Column(db.String(120), unique=True, nullable=False)
    username = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)


    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Planet(db.Model):
    __tablename__ = 'planeta'
    id = db.Column(db.Integer, db.ForeignKey(User.id), primary_key=True)
    planet_name = db.Column(db.String(120), unique=True, nullable=False)
    population = db.Column(db.String(120), unique=True, nullable=False)
    terrain = db.Column(db.String(120), unique=True, nullable=False)
    favplanet_id = db.relationship('User', lazy=True)


    
    def __repr__(self):
        return '<Planet %r>' % self.planet_name

    def serialize(self):
        return {
            "id": self.id,
            "planet_name": self.planet_name,
            # do not serialize the password, its a security breach
        }

class People(db.Model):
    __tablename__ = 'personajes'
    id = db.Column(db.Integer, db.ForeignKey(User.id), primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    last_name = db.Column(db.String(120), unique=True, nullable=False)
    power = db.Column(db.String(120), unique=True, nullable=False)
    favpeople_id = db.relationship('User', lazy=True)


    
    def __repr__(self):
        return '<People %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            # do not serialize the password, its a security breach
        }

class Vehicle(db.Model):
    __tablename__ = 'vehiculos'
    id = db.Column(db.Integer, db.ForeignKey(User.id), primary_key=True)
    brand = db.Column(db.String(120), unique=True, nullable=False)
    capacity = db.Column(db.String(120), unique=True, nullable=False)
    color = db.Column(db.String(120), unique=True, nullable=False)
    favvehicle_id = db.relationship('User', lazy=True)


    
    def __repr__(self):
        return '<Vehicle %r>' % self.brand

    def serialize(self):
        return {
            "id": self.id,
            "brand": self.brand,
            # do not serialize the password, its a security breach
        }