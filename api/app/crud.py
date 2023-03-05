from sqlalchemy.orm import Session
from sqlalchemy import and_

import app.models as models, app.schemas as schemas

def read_playlists(db: Session) -> list[schemas.Playlist]:
    return db.query(models.Playlist).all()

def read_playlist(db: Session, playlist_id: int) -> schemas.Playlist:
    return db.query(models.Playlist).filter(models.Playlist.id == playlist_id).first()

def read_songs(db: Session) -> list[schemas.Song]:
    return db.query(models.Song).all()

def read_song(db: Session, song_id: int) -> schemas.Song:
    return db.query(models.Song).filter(models.Song.id == song_id).first()

def read_connections(db: Session, playlist_id: int, song_id: int) -> list[schemas.Connection]:
    filters = []
    if playlist_id > 0:
        filters.append(lambda: models.Connection.playlist_id == playlist_id)
    if song_id > 0:
        filters.append(lambda: models.Connection.song_id == song_id)
    return db.query(models.Connection).filter(and_(*filters)).all()

def read_connection(db: Session, connection_id: int) -> schemas.Connection:
    return db.query(models.Connection).filter(models.Connection.id == connection_id).first()