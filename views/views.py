from app import create_app
from domain.models import Chirp, User
from serializers.models import ChirpPydanticModel

app, chirp_handler = create_app()


@app.post('/create')
async def create_chirp(chirp: ChirpPydanticModel):
    chirp_handler.create_chirp(

        Chirp(
            User(chirp.author.login, chirp.author.name),
            chirp.text,
            chirp.publish_date
        )
    )
