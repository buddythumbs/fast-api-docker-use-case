from sqlalchemy import Column, String, Numeric, Integer
from sqlalchemy.orm import relationship
import yfinance as yf

from database import Base, SessionLocal

class Stock(Base):
    __tablename__ = "stocks"

    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String, unique=True, index=True)
    price = Column(Numeric(10, 2))
    forward_pe = Column(Numeric(10, 2))
    forward_eps = Column(Numeric(10, 2))
    dividend_yield = Column(Numeric(10, 2))
    ma50 = Column(Numeric(10, 2))
    ma200 = Column(Numeric(10, 2))

def fetch_stock_data(id: int):
    """Take the already added stock from the database and retrieve details from yahoo finance.

    Once the data is retrieved the stock values are updated.
    """

    db = SessionLocal()
    stock = db.query(Stock).filter_by(id=id).first()
    
    yahoo_data=yf.Ticker(stock.symbol)


    stock.ma200 = yahoo_data.info.get('twoHundredDayAverage', 0)
    stock.ma50 = yahoo_data.info.get('fiftyDayAverage', 0)
    stock.price = yahoo_data.info.get('previousClose',0)
    stock.forward_pe = yahoo_data.info.get('forwardPE',0)
    stock.forward_eps = yahoo_data.info.get('forwardEps',0)
    stock.dividend_yield = yahoo_data.info.get('dividendYield',0)
    if stock.dividend_yield is not None:
        stock.dividend_yield =  stock.dividend_yield * 100

    db.add(stock)
    db.commit()

def stock_exists(symbol: str):
    """Check if a symbol is already in the stocks table.

    Return True if symbol is found in the table,
    """

    db = SessionLocal()
    stock = db.query(Stock).filter_by(symbol=symbol).first()
    if stock is not None:
        return True
    else:
        return False
def read_all_stocks():
    """Read all stock information from the stocks table.
    """
    db = SessionLocal()
    stocks = db.query(Stock).all()

    return stocks


