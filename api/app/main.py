from fastapi import FastAPI
import app.models as models
from app.database import engine
from app.routers import playlists, songs, connections

models.Base.metadata.create_all(bind=engine)

main = FastAPI()
app = FastAPI()

app.include_router(playlists.router)
app.include_router(songs.router)
app.include_router(connections.router)

main.mount("/api/v1", app)