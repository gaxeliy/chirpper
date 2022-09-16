from contextlib import contextmanager

from sqlalchemy import ForeignKey, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import sqlalchemy as sa


Base = declarative_base()

engine = create_engine('sqlite:///sqlite.db')

Session = sessionmaker(engine)


@contextmanager
def session_scope():
    session = Session()
    try:
        yield session
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()


class PicturesDb(Base):
    __tablename__ = 'picture'

    id = sa.Column(sa.String, primary_key=True)
    chirp_id = sa.Column(sa.String, ForeignKey('chirp.id'))


class UserDb(Base):
    __tablename__ = 'user'

    id = sa.Column(sa.String, primary_key=True)
    date_of_birth = sa.Column(sa.Date)
    sex = sa.Column(sa.String)
    description = sa.Column(sa.Text)
    login = sa.Column(sa.String)
    avatar = sa.Column(sa.String, ForeignKey('picture.id'))
    name = sa.Column(sa.String)


class ChirpDb(Base):
    __tablename__ = 'chirp'

    id = sa.Column(sa.String, primary_key=True)
    author = sa.Column(sa.String, ForeignKey('user.id'))
    text = sa.Column(sa.Text)
    publish_date = sa.Column(sa.Date)
    is_draft = sa.Column(sa.Boolean)
    is_deleted = sa.Column(sa.Boolean)
    parent = sa.Column(sa.String, ForeignKey('chirp.id'))
    citate = sa.Column(sa.String, ForeignKey('chirp.id'))
