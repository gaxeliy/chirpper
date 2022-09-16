from abc import ABC

from domain.models import Chirp


class AbstractDatabase(ABC):
    def read_chirp_from_db(self, uuid):
        raise NotImplemented

    def save_chirp_to_db(self, chirps: list[Chirp]):
        raise NotImplemented


class MockDb(AbstractDatabase):
    def __init__(self):
        self.chirps = {}

    def read_chirp_from_db(self, uuid) -> Chirp:
        return self.chirps[uuid]

    def save_chirp_to_db(self, chirps: list[Chirp]):
        for chirp in chirps:
            self.chirps[chirp.uuid] = chirp


class SqliteDb(AbstractDatabase):
    def __init__(self):
        pass

    def read_chirp_from_db(self, uuid) -> Chirp:
        pass

    def save_chirp_to_db(self, chirps: list[Chirp]):
        pass
