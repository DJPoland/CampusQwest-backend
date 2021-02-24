from typing import TypedDict

class User(TypedDict):
    id: str
    avatar: str
    badges: list
    banner: str
    campus: str
    exp: int
    username: str
    trophies: list
    qwestLines: list

class CurrentQwest(TypedDict):
    locationIndex = str
    qwestId = str
    timeStarted = str