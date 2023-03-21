import json
from fastapi import FastAPI
import app.models as models
from app.database import engine
from app.routers import playlists, songs, connections
from prometheus_fastapi_instrumentator import Instrumentator

models.Base.metadata.create_all(bind=engine)

main = FastAPI()
Instrumentator().instrument(main).expose(main)

app = FastAPI(openapi_tags=json.load(open("./app/metadata.json")))
app.include_router(playlists.router)
app.include_router(songs.router)
app.include_router(connections.router)

main.mount("/api/v1", app)