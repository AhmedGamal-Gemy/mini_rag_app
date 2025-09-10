from fastapi import FastAPI
from routes import base,data
from helpers.init_db import init_database

from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app : FastAPI):

    # Before the app receiveing requests
    app.mongo_conn, app.db_client = await init_database()

    yield

    # After the app ends
    await app.mongo_conn.close()


app = FastAPI( lifespan = lifespan )

app.include_router( base.base_router )
app.include_router( data.data_router )

