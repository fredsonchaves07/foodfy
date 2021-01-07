from . import db
from datetime import datetime
from sqlalchemy.dialects.postgresql import ARRAY


class File(db.Model):
    __tablename__ = 'FFILES'
    id = db.Column('ID', db.Integer, primary_key=True)
    name = db.Column('NAME', db.String(100), nullable=False)
    path = db.Column('PATH', db.String(100), nullable=False)
    created_at = db.Column('CREATEDAT', db.DateTime, nullable=False, default=datetime.utcnow)
    modified_at = db.Column('MODIFIEDAT', db.DateTime, nullable=False, default=datetime.utcnow) 


class Chef(db.Model):
    __tablename__ = 'FCHEF'
    id = db.Column('ID', db.Integer, primary_key=True)
    name = db.Column('NAME', db.String(100), nullable=False)
    file_id = db.Column('FILEID', db.Integer, db.ForeignKey('FFILES.ID'))
    created_at = db.Column('CREATEDAT', db.DateTime, nullable=False, default=datetime.utcnow)
    modified_at = db.Column('MODIFIEDAT', db.DateTime, nullable=False, default=datetime.utcnow)

    file = db.relationship("File", foreign_keys=file_id)


class Recipe(db.Model):
    __tablename__ = 'FRECIPE'
    id = db.Column('ID', db.Integer, primary_key=True)
    name = db.Column('NAME', db.String(100), nullable=False)
    chef_id = db.Column('CHEFID', db.Integer, db.ForeignKey('FCHEF.ID'))
    ingredients= db.Column('INGREDIENTS', ARRAY(db.Text), nullable=False)
    preparations = db.Column('PREPARATIONS', ARRAY(db.Text), nullable=False)
    adicional_information = db.Column('ADDICIONALINFORMATIONS', db.Text)
    created_at = db.Column('CREATEDAT', db.DateTime, nullable=False, default=datetime.utcnow)
    modified_at = db.Column('MODIFIEDAT', db.DateTime, nullable=False, default=datetime.utcnow)

    chef = db.relationship("File", foreign_keys=chef_id)