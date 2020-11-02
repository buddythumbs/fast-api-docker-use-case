from fastapi import APIRouter, HTTPException, Depends, BackgroundTasks
from database import SessionLocal, get_db
from schemas.stocks import StockRequest
from models.stocks import Stock, fetch_stock_data, stock_exists, read_all_stocks
from sqlalchemy.orm import Session

router = APIRouter()

@router.get("/")
def read_stocks(db: Session = Depends(get_db)):
    """Reads and returns a list of stocks in the database.
    """

    stocks = read_all_stocks()

    return stocks

@router.post("/")
async def create_stock(stock_request: StockRequest, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    """Adds a new stock to track to the database.
    """

    if stock_exists(stock_request.symbol):
        return { "symbol": stock_request.symbol, "message": "Stock already added " }

    stock = Stock(symbol=stock_request.symbol)
    db.add(stock)
    db.commit() 

    background_tasks.add_task(fetch_stock_data, stock.id)

    return { "symbol": stock.symbol, "id": stock.id }