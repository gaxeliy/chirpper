from fastapi import FastAPI

from repository.db import MockDb
from use_cases.use_cases import ChirpHandler


def create_app():
    app = FastAPI()
    db = MockDb()
    chirp_handler = ChirpHandler(db)
    return (app, chirp_handler)
