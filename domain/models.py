import datetime
import uuid
from enum import Enum


class Sex(Enum):
    male = 1
    female = 2


class Picture:
    ...


class User:
    def __init__(
            self,
            login: str,
            name: str,
            sex: Sex = None,
            date_of_birth: datetime.datetime = None,
            description: str = '',
            avatar: Picture = None,
            pictures: list[Picture] = None
    ):
        self.id = uuid.uuid4()
        self.date_of_birth = date_of_birth
        self.sex = sex
        self.description = description
        self.login = login
        self.pictures = pictures
        self.avatar = avatar
        self.name = name


class Chirp:
    def __init__(
            self,
            author: User,
            text: str,
            publish_date: datetime.datetime,
            is_draft: bool = False,
            is_deleted: bool = False,
            replies: list['Chirp'] = None,
            pictures: list[Picture] = None,
            parent: 'Chirp' = None,
            citate: 'Chirp' = None,
    ):
        self.uuid = uuid.uuid4()
        self.pictures = pictures
        self.is_draft = is_draft
        self.is_deleted = is_deleted
        self.citate = citate
        self.parent = parent
        self.author = author
        self.text = text
        if replies:
            self.replies = replies
        else:
            self.replies = []
        self.publish_date = publish_date

    def __eq__(self, other: 'Chirp'):
        return self.uuid == other.uuid
