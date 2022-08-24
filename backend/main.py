from fastapi import FastAPI
import backend.routers.router as hw_router

app = FastAPI()

app.include_router(hw_router.router)