from database import db
from datetime import datetime

class Meal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=False, default="")
    datetime = db.Column(db.DateTime(), nullable=False, default=datetime.now())
    is_diet = db.Column(db.Boolean(), nullable=False, default=True)
