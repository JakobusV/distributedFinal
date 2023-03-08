from fastapi import Depends, APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from ..database import get_db
from ..stream import send_json, topic
from .. import crud, schemas

table = "songs"
router = APIRouter(
    prefix="/songs",
)

@router.get("/", response_model=list[schemas.Song])
def read_songs(db: Session = Depends(get_db)):
    db_songs = crud.read_songs(db)
    return db_songs

@router.get("/{song_id}", response_model=schemas.Song)
def read_song(song_id: int, db: Session = Depends(get_db)):
    db_song = crud.read_song(db, song_id=song_id)
    if db_song == None:
        raise HTTPException(status_code=404, detail="Song not found")
    return db_song

@router.post("/")
def create_song(song: schemas.SongCreate):
    # send post message to stream
    data = {
        "table": table,
        "action": "create",
        "data": jsonable_encoder(song)
    }
    send_json(topic=topic, data=data)
    return

@router.patch("/{song_id}")
def update_song(song_id: int, song: schemas.SongCreate, db: Session = Depends(get_db)):
    read_song(song_id, db)
    # send patch message to stream
    data = {
        "table": table,
        "action": "patch",
        "data": {
                "song_id": song_id,
                "song": jsonable_encoder(song)
            }
    }
    send_json(topic=topic, data=data)
    return

@router.delete("/{song_id}")
def remove_song(song_id: int, db: Session = Depends(get_db)):
    read_song(song_id, db)
    # send delete to stream
    data = {
        "table": table,
        "action": "delete",
        "data": song_id
    }
    send_json(topic=topic, data=data)
    return