from typing import List, Union

from pydantic import BaseModel


class PaginatedData(BaseModel):
    data: List
    page_num: int
    page_size: int
    total: int


class PlayerStat(BaseModel):
    id: str
    player: str
    team: str
    pos: str
    att: float
    att_g: float
    yds: float
    avg: float
    yds_g: float
    td: float
    lng: Union[float, str]
    first: float
    first_percentage: float
    twenty_plus: float
    forty_plus: float
    fum: float
