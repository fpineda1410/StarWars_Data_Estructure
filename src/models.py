import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    created_at = Column(String(250), nullable=False)
    updated_at = Column(String(250), nullable=True)

class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    planet_name = Column(String(250), nullable=False)
    planet_climate = Column(String(250), nullable=True)
    planet_diameter = Column(Integer, nullable=True)
    planet_population = Column(Integer, nullable=True)
    planet_gravity = Column(Integer, nullable=True)
    planet_terrain = Column(String(250), nullable=True)
    planet_url = Column(String(250), nullable=True)

class Protagonists(Base):
    __tablename__ = 'protagonists'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    protagonists_name = Column(String(250), nullable=False)
    protagonists_gender = Column(String(250), nullable=True)
    protagonists_birthyear = Column(String(250), nullable=True)
    protagonists_eyecolor = Column(String(250), nullable=True)
    protagonists_haircolor = Column(String(250), nullable=True)
    protagonists_homeworld = Column(String(250), nullable=True)
    protagonists_height = Column(Integer, nullable=True)
    planet_url = Column(String(250), nullable=True)

class User_Favorites(Base):
    __tablename__ = 'user_favorites'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    protagonists_id = Column(Integer, ForeignKey('protagonists.id'))
    planets_id = Column (Integer, ForeignKey('planets.id'))

# class Share_Data(Base):
#     __tablename__ = 'share_data'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     user_id = Column(Integer, ForeignKey('user.id'))
#     facebook_account=Column(String(250),nullable=True)
#     instagram_account=Column(String(250),nullable=False)
#     data_id=Column (Integer,ForeignKey('user_favorites.id'))
#     def to_dict(self):
#         return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')