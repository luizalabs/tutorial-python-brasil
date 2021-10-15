import json
import os
from pathlib import Path
from random import random

from fastapi import FastAPI, HTTPException
from fastapi import status
from fastapi.responses import JSONResponse

DATA_DIR = Path(os.path.dirname(__file__)) / "data"
FAIL_RATE = int(os.getenv("FAIL_RATE", 0))


app = FastAPI()


@app.middleware("http")
async def controlled_fail_middleware(request, call_next):
    if FAIL_RATE / 100 > random():
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return await call_next(request)


def read_data(file_):
    return json.load(open(file_))


@app.get("/catalogs")
async def catalog_list():
    files = DATA_DIR.glob("*.json")
    return [read_data(f_) for f_ in files]


@app.get("/catalogs/{code}")
async def catalog_retrieve(code):
    try:
        return read_data(DATA_DIR / f"{code}.json")
    except FileNotFoundError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
