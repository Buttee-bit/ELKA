from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from prometheus_fastapi_instrumentator import Instrumentator

import logging

from .set_loggin import LoggerSetup
logger_setup = LoggerSetup()
LOGGER = logging.getLogger(__name__)

app = FastAPI(
    title="ELKA API"
)

origins = [
    "http://localhost",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
    LOGGER.info("--- Start up App ---")
    pass

@app.on_event("shutdown")
async def shutdown():
    LOGGER.info("--- shutdown App ---")
    pass
