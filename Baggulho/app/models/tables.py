from app import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    name = db.Column(db.String)
    email = db.Column(db.String, unique=True)

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def __init__(self, username, password, name, email):
        self.username = username
        self.password = password
        self.name = name
        self.email = email

    def __repr__(self):
        return "<User %r>" % self.usarname

class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    types = db.Column(db.String)
    brand = db.Column(db.String)
    description = db.Column(db.String)
    specifications = db.Column(db.String)
    img = db.Column(db.String)
    price = db.Column(db.Float)
    unit = db.Column(db.Integer) 

    def __init__(self, name, types, brand, description, specifications, img, price, unit):
        self.name = name
        self.types = types
        self.brand = brand
        self.description = description
        self.specifications = specifications
        self.img = img
        self.price = price
        self.unit = unit

    def __repr__(self):
        return "<Product %r>" % self.name

class Image(db.Model):
    __tablename__ = "images"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    img = db.Column(db.String)

    def __init__(self, img, name):
        self.img = img
        self.name = name

    def __repr__(self):
        return "<Image %r>" % self.img

class Sale(db.Model):
    __tablename__ = "Sales"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    item_id = db.Column(db.Integer, db.ForeignKey("products.id"))
    num_item = db.Column(db.Integer)
    amount = db.Column(db.Float)

    buyer = db.relationship("User", foreign_keys=user_id)
    product_sold = db.relationship("Product", foreign_keys=item_id)

    def __init__(self, user_id, item_id, num_item, amount):
        self.user_id = user_id
        self.item_id = item_id
        self.num_item = num_item
        self.amount = amount

    def __repr__(self):
        return "<Sale %r>" % self.id