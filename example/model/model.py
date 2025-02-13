from typing import List
from pydantic import BaseModel


class VenueData(BaseModel):
    venue: str
    description: str


class Response(BaseModel):
    data: List[VenueData]
