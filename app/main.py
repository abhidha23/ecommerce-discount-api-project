from fastapi import FastAPI
from app.routers.coupons import router  
import sys
import os

app = FastAPI()

app.include_router(router)