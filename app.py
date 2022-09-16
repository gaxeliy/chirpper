from fastapi import FastAPI

from repository.db import MockDb, SqliteDb
from use_cases.use_cases import ChirpHandler


def create_app():
    app = FastAPI()
    db = SqliteDb()
    chirp_handler = ChirpHandler(db)
    return app, chirp_handler
