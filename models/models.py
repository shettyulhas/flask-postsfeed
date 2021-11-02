from sqlalchemy import Column, Text, ForeignKey, Integer
from sqlalchemy.orm import relationship
from .base import Base


class User(Base):
    __tablename__ = 'u_user'
    username = Column(Text)
    user_uuid = Column(Text, primary_key=True)
    profile = relationship('Profile', backref='user', uselist=False)


class Profile(Base):
    __tablename__ = 'u_profile'
    first_name = Column(Text)
    last_name = Column(Text)
    user_uuid = Column(Text, ForeignKey(User.user_uuid), primary_key=True)

### Create Post DB table, u_post, to add the user post feeds
class Post(Base):
    __tablename__ = 'u_post'
    caption = Column(Text)
    followers = Column(Integer)
    image_url = Column(Text)
    likes = Column(Integer)
    profile_image_url = Column(Text)
    title = Column(Text)
    username = Column(Text, primary_key=True)