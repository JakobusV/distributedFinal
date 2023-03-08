from fastapi import Depends, APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from . playlists import read_playlist
from . songs import read_song
from ..database import get_db
from ..stream import send_json, topic
from .. import crud, schemas

table = "connections"
router = APIRouter(
    prefix="/connections",
)

@router.get("/", response_model=list[schemas.MetaConnection])
def read_connections(playlist_id: int = 0, song_id: int = 0, db: Session = Depends(get_db)):
    db_connections = crud.read_connections(db, playlist_id=playlist_id, song_id=song_id)
    if len(db_connections) < 0:
        raise HTTPException(status_code=404, detail="No connections found")
    return db_connections

@router.get("/{connection_id}", response_model=schemas.MetaConnection)
def read_connection(connection_id: int, db: Session = Depends(get_db)):
    db_connection = crud.read_connection(db, connection_id=connection_id)
    if db_connection == None:
        raise HTTPException(status_code=404, detail="Connection not found")
    return db_connection

@router.post("/")
def create_connection(connection: schemas.ConnectionCreate, db: Session = Depends(get_db)):
    read_playlist(connection.playlist_id, db)
    read_song(connection.song_id, db)
    # send post message to stream
    data = {
        "table": table,
        "action": "create",
        "data": jsonable_encoder(connection)
    }
    send_json(topic=topic, data=data)
    return

@router.delete("/{connection_id}")
def remove_connection(connection_id: int, db: Session = Depends(get_db)):
    read_connection(connection_id, db)
    # send delete to stream
    data = {
        "table": table,
        "action": "delete",
        "data": connection_id
    }
    send_json(topic=topic, data=data)
    return