from fastapi import Depends, APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from ..database import get_db
from ..stream import send_json, topic
from .. import crud, schemas

table = "playlists"
router = APIRouter(
    tags = [table],
    prefix="/playlists",
)

@router.get("/", response_model=list[schemas.Playlist])
def read_playlists(db: Session = Depends(get_db)):
    db_playlists = crud.read_playlists(db)
    return db_playlists

@router.get("/{playlist_id}", response_model=schemas.Playlist)
def read_playlist(playlist_id: int, db: Session = Depends(get_db)):
    db_playlist = crud.read_playlist(db, playlist_id=playlist_id)
    if db_playlist == None:
        raise HTTPException(status_code=404, detail="Playlist not found")
    return db_playlist

@router.post("/")
def create_playlist(playlist: schemas.PlaylistCreate):
    # send post message to stream
    data = {
        "table": table,
        "action": "create",
        "data": jsonable_encoder(playlist)
    }
    send_json(topic=topic, data=data)
    return

@router.patch("/{playlist_id}")
def update_playlist(playlist_id: int, playlist: schemas.PlaylistCreate, db: Session = Depends(get_db)):
    read_playlist(playlist_id, db)
    # send patch message to stream
    data = {
        "table": table,
        "action": "update",
        "data": {
                "playlist_id": playlist_id,
                "playlist": jsonable_encoder(playlist)
            }
    }
    send_json(topic=topic, data=data)
    return

@router.delete("/{playlist_id}")
def remove_playlist(playlist_id: int, db: Session = Depends(get_db)):
    read_playlist(playlist_id, db)
    # send delete to stream
    data = {
        "table": table,
        "action": "delete",
        "data": playlist_id
    }
    send_json(topic=topic, data=data)
    return