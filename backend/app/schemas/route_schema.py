from pydantic import BaseModel

class RouteRequest(BaseModel):
    start: str
    end: str
    profile: str
    avoid_stairs: bool
    need_audio: bool
    avoid_crowds: bool

class RouteResponse(BaseModel):
    distance: float
    safety_score: float
    accessibility_score: float