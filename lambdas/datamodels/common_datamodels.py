@marshmallow_dataclass
class User:
    id: str
    avatar: str
    badges: list
    banner: str
    campus: str
    exp: int
    username: str
    trophies: list
    qwestLines: list

@marshmallow_dataclass
class CurrentQwest:
    locationIndex: str
    qwestId: str
    timeStarted: str