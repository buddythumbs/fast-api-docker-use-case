from fastapi import FastAPI
from sqlalchemy.orm import Session 

from database import Base, engine
from models.stocks import Stock
from routes import stocks

app = FastAPI()

# Create all tables specified in all models
Base.metadata.create_all(bind=engine)

app.include_router(
    stocks.router,
    tags=["Stocks"],
    prefix="/stocks",
    responses={404: {"description": "Not found"}},
)