import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    username_id = Column(Integer, primary_key=True)
    first_name = Column(String(50))
    last_name= Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)

class Followers(Base):
    __tablename__ = 'Followers'
    user_form_id = Column(Integer, primary_key=True)
    user_to_id = Column(Integer, nullable=False)
    email_followers = Column(String(250),ForeignKey(User.email))
    rel = relationship(User)

class Comment(Base):
    __tablename__ = 'Comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250))
    author_id = Column(Integer,ForeignKey(User.username_id))
    post_ID =  Column(Integer)
    rel= relationship (User)
    
class Post(Base):
    __tablename__ = 'Post'
    id = Column(Integer, primary_key=True,)
    user_ID = Column(String(50), ForeignKey(User.first_name))
    rel_id_com =Column(Integer, ForeignKey(Comment.id))
    rel = relationship(Comment)
    rel_dos =relationship(User)
   
class Media(Base):
    __tablename__ = 'Media'
    id = Column(Integer, primary_key=True)
    Type= Column(String(50), nullable=False )
    Url= Column(String(250),ForeignKey(Post.user_ID))
    post_id= Column(Integer, nullable=False)
    rel = relationship(Post)
    
    















# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')