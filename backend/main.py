from fastapi import FastAPI
from routers import router as hw_router

app = FastAPI()

app.include_router(hw_router.router)