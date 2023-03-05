from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import app.crud as crud
import app.models as models
import app.schemas as schemas
from app.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/playlists", response_model=list[schemas.Playlist])
def read_playlists(db: Session = Depends(get_db)):
    db_playlists = crud.read_playlists(db)
    return db_playlists
@app.get("/playlists/{playlist_id}", response_model=schemas.Playlist)
def read_playlist(playlist_id: int, db: Session = Depends(get_db)):
    db_playlist = crud.read_playlist(db, playlist_id=playlist_id)
    if db_playlist == None:
        raise HTTPException(status_code=404, detail="Playlist not found")
    return db_playlist

@app.post("/playlists")
def create_playlist(playlist: schemas.PlaylistCreate):
    # send post message to stream
    pass
@app.patch("/playlists/{playlist_id}")
def update_playlist(playlist_id: int, playlist: schemas.PlaylistCreate):
    db_playlist = read_playlist(playlist_id)
    # send patch message to stream
    pass
@app.delete("/playlists/{playlist_id}")
def remove_playlist(playlist_id: int):
    db_playlist = read_playlist(playlist_id)
    # send delete to stream
    pass


@app.get("/songs", response_model=list[schemas.Song])
def read_songs(db: Session = Depends(get_db)):
    db_songs = crud.read_songs(db)
    return db_songs
@app.get("/songs/{song_id}", response_model=schemas.Song)
def read_song(song_id: int, db: Session = Depends(get_db)):
    db_song = crud.read_song(db, song_id=song_id)
    if db_song == None:
        raise HTTPException(status_code=404, detail="Song not found")
    return db_song

@app.post("/songs")
def create_song(song: schemas.SongCreate):
    # send post message to stream
    pass
@app.patch("/songs/{song_id}")
def update_song(song_id: int, song: schemas.SongCreate):
    db_song = read_song(song_id)
    # send patch message to stream
    pass
@app.delete("/songs/{song_id}")
def remove_song(song_id: int):
    db_song = read_song(song_id)
    # send delete to stream
    pass


@app.get("/connections", response_model=list[schemas.Connection])
def read_connections(playlist_id: int = 0, song_id: int = 0, db: Session = Depends(get_db)):
    db_connections = crud.read_connections(db, playlist_id=playlist_id, song_id=song_id)
    if len(db_connections) < 0:
        raise HTTPException(status_code=404, detail="No connections found")
    return db_connections
@app.get("/connections/{connection_id}", response_model=schemas.Connection)
def read_connection(connection_id: int, db: Session = Depends(get_db)):
    db_connection = crud.read_connection(db, connection_id=connection_id)
    if db_connection == None:
        raise HTTPException(status_code=404, detail="Connection not found")
    return db_connection

@app.post("/connections")
def create_connection(connection: schemas.ConnectionCreate):
    # send post message to stream
    pass
@app.delete("/connections/{connection_id}")
def remove_connection(connection_id: int):
    db_connection = read_connection(connection_id)
    # send delete to stream
    pass