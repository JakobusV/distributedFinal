from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base

class Playlist(Base):
    __tablename__ = 'playlists'

    playlist_id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    created_date = Column(String, nullable=False)
    details = Column(String)
    image_url = Column(String)

class Song(Base):
    __tablename__ = 'songs'

    song_id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    artist = Column(String, nullable=False)
    album = Column(String, nullable=False)
    duration = Column(Integer, nullable=False)

class Connection(Base):
    __tablename__ = 'connections'

    connection_id = Column(Integer, primary_key=True, nullable=False)
    playlist_id = Column(Integer, ForeignKey('playlists.playlist_id'), nullable=False)
    song_id = Column(Integer, ForeignKey('songs.song_id'), nullable=False)
