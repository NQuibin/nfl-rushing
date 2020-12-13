from typing import Optional

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pymongo import ASCENDING, DESCENDING

from .manager import PlayerStatsManager
from .models import PaginatedData

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:8080'],
    allow_methods=['*'],
    allow_headers=['*']
)

manager = PlayerStatsManager()


@app.exception_handler(Exception)
async def validation_exception_handler(_, exc):
    status_code = getattr(exc, 'status_code', 500)
    message = getattr(exc, 'message', 'Something went wrong')
    return JSONResponse(status_code=status_code, content={'message': message})


@app.get('/v1/player-stats', response_model=PaginatedData)
def get_player_stats(
        player: Optional[str] = None,
        sort_field: Optional[str] = 'player',
        ascending: bool = True,
        page_num: Optional[int] = 1,
        page_size: Optional[int] = 25
):
    order = ASCENDING if ascending else DESCENDING
    return manager.find_all(
        player=player,
        sort_field=sort_field,
        order=order,
        page_num=page_num,
        page_size=page_size
    )


