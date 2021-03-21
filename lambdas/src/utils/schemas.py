from typing import TypedDict

class User(TypedDict):
    id: str
    campus: str
    exp: int
    rank: str
    selectedAvatar: int 
    selectedBanner: int
    trophies: list
    medals: list
    username: str
    currentQwests: list
    qwestsCompleted: list


class CurrentQwest(TypedDict):
    qwestId = str
    locationIndex = str
    timeStarted = str