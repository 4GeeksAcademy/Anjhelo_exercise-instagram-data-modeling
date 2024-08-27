import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class Media(Base):
    __tablename__ = "media"

    Id = Column(Integer, primary_key=True)
    type = Column(Enum("Photo", "Video", name="type"))
    url = Column(String(80))
    post_id = Column(Integer, ForeignKey("post.Id"))



class Post(Base):
    __tablename__ = "post"

    Id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.Id"))
    medias = relationship("Media", backref = "post")
    comments = relationship("Comment", backref = "post")

class User(Base):
    __tablename__ = "user"

    Id = Column(Integer, primary_key=True)
    username = Column(String(30))
    firstname = Column(String(30))
    lastname = Column(String(50))
    email = Column(String(50))
    posts = relationship("Post", backref = "User")
    comments = relationship("Comment", backref = "user")
    followers = relationship("Follower", foreign_keys="Follower.user_from_id", backref="user_from")
    following = relationship("Follower", foreign_keys="Follower.user_to_id", backref="user_to")

class Comment(Base):
    __tablename__ = "comment"

    Id = Column(Integer, primary_key=True)
    comment_text = Column(String(100))
    user_id = Column(Integer, ForeignKey("user.Id"))
    post_id = Column(Integer, ForeignKey("post.Id"))

class Follower(Base):
    __tablename__ = "follower"

    user_from_id = Column(Integer, ForeignKey("user.Id"), primary_key=True)
    user_to_id = Column(Integer, ForeignKey("user.Id"), primary_key=True)


## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
