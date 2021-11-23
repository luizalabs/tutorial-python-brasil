import json
import os
from pathlib import Path
from uuid import UUID
from random import random


from fastapi import FastAPI, HTTPException, Header, status
from fastapi.param_functions import Depends
from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter
from starlette.responses import PlainTextResponse

DATA_DIR = Path(os.path.dirname(__file__)) / "data"
FAIL_RATE = int(os.getenv("FAIL_RATE", 0))


async def verify_x_tenant_id(x_tenant_id: str = Header(...)):
    if x_tenant_id != "21fea73c-e244-497a-8540-be0d3c583596":
        raise HTTPException(status.HTTP_403_FORBIDDEN, detail={"message": "Tenant ID not on tenants list"})
    return x_tenant_id

async def verify_apikey(x_api_key: str = Header(...)):
    if x_api_key != "5734143a-595d-405d-9c97-6c198537108f":
        raise HTTPException(status.HTTP_403_FORBIDDEN, detail="Unauthorized")
    return x_api_key


app = FastAPI(dependencies=[Depends(verify_apikey)])
maestro = APIRouter(dependencies=[Depends(verify_x_tenant_id)])
account = APIRouter()
catalogs = APIRouter()


@app.middleware("http")
async def controlled_fail_middleware(request, call_next):
    if FAIL_RATE / 100 > random():
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return await call_next(request)


def read_data(file_):
    return json.load(open(file_))


@catalogs.get("/catalogs", tags=["catalogs"])
async def catalog_list():
    files = (DATA_DIR / "catalogo").glob("*.json")
    return [read_data(f_) for f_ in files]


@catalogs.get("/catalogs/{code}", tags=["catalogs"])
async def catalog_retrieve(code):
    try:
        return read_data(DATA_DIR / "catalogo" /  f"{code}.json")
    except FileNotFoundError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@account.get("/account/v1/whoami", tags=["account"])
def whoami():
    return read_data(DATA_DIR / "account" / "whoami.json")


@account.get("/account/v1/whoami/tenants", tags=["account"])
def whoami_tenants():
    return read_data(DATA_DIR / "account" / "whoami_tenants.json")


@maestro.get("/maestro/v1/orders", tags=["maestro"])
def orders(_limit: int = 10, _offset: int = 0):
    if _limit != 10:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Limit must be 10")
    if _offset % 10 != 0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Offset must be multiple of 10")
    try:
        return read_data(DATA_DIR / "maestro" / "orders" / f"sample{_offset}.json")
    except FileNotFoundError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=read_data(DATA_DIR / "maestro" / "orders" / "not_found.json"))


@maestro.get("/maestro/v1/orders/{order_id}", tags=["maestro"])
def order(order_id: UUID):
    try:
        return read_data(DATA_DIR / "maestro" / "order" / f"{order_id}.json")
    except FileNotFoundError:
        error = read_data(DATA_DIR / "maestro" / "order" / "not_found.json")
        error[0]["details"][0]["value"] = str(order_id)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error)


@maestro.get("/maestro/v1/orders/{order_id}/packages/{package_id}", tags=["maestro"])
def packages(order_id: UUID, package_id: UUID):
    try:
        return read_data(DATA_DIR / "maestro" / "packages" / f"{order_id}{package_id}.json")
    except FileNotFoundError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=read_data(DATA_DIR / "maestro" / "packages" / "not_found.json"))


@maestro.get("/maestro/v1/orders/{order_id}/packages/{package_id}/items", tags=["maestro"])
def package_items(order_id: UUID, package_id: UUID):
    try:
        return read_data(DATA_DIR / "maestro" / "package_items" / f"{order_id}{package_id}.json")
    except FileNotFoundError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=read_data(DATA_DIR / "maestro" / "package_items" / "not_found.json"))

app.include_router(maestro)
app.include_router(account)
app.include_router(catalogs)