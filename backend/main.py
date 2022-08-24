from fastapi import FastAPI
from .routers import hw_router

app = FastAPI()

app.include_router(hw_router.router)