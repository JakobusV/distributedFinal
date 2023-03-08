from typing import Optional

from pydantic import BaseModel

class BasePlaylist(BaseModel):
    title: str
    created_date: str
    details: Optional[str] = None
    image_url: Optional[str] = None
class PlaylistCreate(BasePlaylist):
    pass
class Playlist(BasePlaylist):
    playlist_id: int
    class Config:
        orm_mode = True

class BaseSong(BaseModel):
    title: str
    artist: str
    album: str
    duration: int
class SongCreate(BaseSong):
    pass
class Song(BaseSong):
    song_id: int
    class Config:
        orm_mode = True

class BaseConnection(BaseModel):
    playlist_id: int
    song_id: int
class ConnectionCreate(BaseConnection):
    pass
class Connection(BaseConnection):
    connection_id: int
    class Config:
        orm_mode = True
class MetaConnection(BaseConnection):
    connection_id: int
    playlist: str
    song: str