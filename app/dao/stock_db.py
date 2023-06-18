from app.model.stock import Stock
from app.dao.db_operation import Db_sqlite

def insert_in_stocks_table(o:Stock):
    table_stocks = "stocks"
    cmd = "('" + o.stock_name +"', '" + o.stock_symbol + "', " + str(o.price) + ")"
    Db_sqlite().insert(table_stocks, cmd)

def delete_in_stocks_table(column:str, search_data:str):
    table_stocks = "stocks"
    Db_sqlite().delete(table_stocks, column, search_data)

def get_stock_in_table(symbol:str) -> list:
    table_stocks = "stocks"
    return Db_sqlite().get_select_table_data(table_stocks, "symbol", symbol)

def update_price(symbol:str, new_price:float):
    stocks = "stocks"
    search_symbol = "'" + symbol + "'"
    Db_sqlite().update_value(stocks, "symbol", search_symbol, "price", str(new_price))

def get_stocks()->list:
    table_stocks = "stocks"
    return Db_sqlite().get_selected_table(table_stocks)

