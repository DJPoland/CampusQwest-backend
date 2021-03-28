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
    currentQwest: dict
    qwestsCompleted: list


class CurrentQwest(TypedDict):
    qwestId = str
    locationIndex = int
    timeStarted = str
    numOfLocations = int