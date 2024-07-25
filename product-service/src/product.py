from db import db # Import from db.py to get access to SQLAlchemy

class Product(db.Model):
    __tablename__ = 'products'

    # Table columns
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))

    def __init__(self, id, name) -> None:
        self.id = id
        self.name = name

    @classmethod
    def find_by_name(cls, _name):
        return cls.query.filter(cls.name == _name)

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.get(_id)
    
    @classmethod
    def find_all(cls):
        return cls.query.all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @property
    def json(self):
        return {
            "id": self.id,
            "name": self.name
        }