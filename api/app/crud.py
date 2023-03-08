import os
from sqlalchemy.orm import Session
from sqlalchemy import and_

import app.models as models, app.schemas as schemas

def read_playlists(db: Session) -> list[schemas.Playlist]:
    return db.query(models.Playlist).all()

def read_playlist(db: Session, playlist_id: int) -> schemas.Playlist:
    return db.query(models.Playlist).filter(models.Playlist.playlist_id == playlist_id).first()

def read_songs(db: Session) -> list[schemas.Song]:
    return db.query(models.Song).all()

def read_song(db: Session, song_id: int) -> schemas.Song:
    return db.query(models.Song).filter(models.Song.song_id == song_id).first()

def read_connections(db: Session, playlist_id: int, song_id: int) -> list[schemas.MetaConnection]:
    filters = []
    if playlist_id > 0:
        filters.append(lambda: models.Connection.playlist_id == playlist_id)
    if song_id > 0:
        filters.append(lambda: models.Connection.song_id == song_id)
    
    db_connections = db.query(models.Connection).filter(and_(*filters)).all()
    
    connections = []
    
    for db_connection in db_connections:
        connections.append(unwrap_connection(db_connection))
    
    return connections

def read_connection(db: Session, connection_id: int) -> schemas.MetaConnection:
    db_connection = db.query(models.Connection).filter(models.Connection.connection_id == connection_id).first()
    
    connection = unwrap_connection(db_connection)
    
    return connection


def unwrap_connection(model: models.Connection) -> schemas.MetaConnection:
    '''
    Creates a new schemas.MetaConnection object from a database model.
    '''
    
    API_URL = os.environ.get('API_URL')
    
    return schemas.MetaConnection(
        connection_id = model.connection_id,
        playlist_id = model.playlist_id,
        song_id = model.song_id,
        playlist = API_URL + f'/playlists/{model.playlist_id}',
        song = API_URL + f'/songs/{model.song_id}'
    )