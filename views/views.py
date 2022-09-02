from fastapi import FastAPI
import uvicorn

from domain.models import Chirp, User
from repository.db import MockDb
from serializers.models import ChirpPydanticModel
from use_cases.use_cases import ChirpHandler

app = FastAPI()

db = MockDb()
chirp_handler = ChirpHandler(db)


@app.post('/create')
async def create_chirp(chirp: ChirpPydanticModel):
    chirp_handler.create_chirp(

        Chirp(
            User(chirp.author.login, chirp.author.name),
            chirp.text,
            chirp.publish_date
        )
    )


if __name__ == '__main__':
    uvicorn.run(app)