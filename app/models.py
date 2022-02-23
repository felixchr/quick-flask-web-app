import datetime

from app import db

from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.sql import func
from werkzeug.security import generate_password_hash, check_password_hash

class Config(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    target = db.Column(db.String(255))
    key = db.Column(db.String(255))
    value = db.Column(db.String(2048))
    col1 = db.Column(db.String(255))
    col2 = db.Column(db.String(255))
    col3 = db.Column(db.String(255))
    col4 = db.Column(db.String(255))
    col5 = db.Column(db.String(255))

