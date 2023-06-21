from flask import jsonify, request, json, render_template
from app.dao.stock_db import *
from app.postman.collection import download

def home_page():
    return render_template("home_page.html")

def collection():
    return download

def stocks_in_data_base():
    response = []
    for obj in get_stocks():
        response.append({
                            "Name": obj[0],
                            "Symbol": obj[1],
                            "Price": obj[2]
                        })
    stocks = {"Stocks": response}
    if len(response) == 0:
        return response_pattern(404, "there are NOT stocks in the database", stocks)
    return response_pattern(200, "there are stocks in the database", stocks)

def search_stock(symbol):
    response = []
    for obj in get_stock_in_table(symbol):
        if symbol==obj[1]:
            response.append({
                                "Name": obj[0],
                                "Symbol": obj[1],
                                "Price": obj[2]
                            })
            stock = {"Stock": response}
            return response_pattern(200, f"there are a stock with symbol {symbol} in database", stock)
    return response_pattern(400, "there are NOT a stock with this symbol in database", None)

def new_stock(data):
    for obj in get_stock_in_table(data['Symbol']):
        if len(obj) > 0:
            return response_pattern(409, "it was not possible to create a new action because the symbol is already in use", None)
    insert_in_stocks_table(Stock(data['Name'], data['Symbol'], data['Price']))
    return response_pattern(201, "new stock created", None)

def change_stock_price(symbol:str, data):
    for obj in get_stock_in_table(symbol):
        if symbol==obj[1]:
            update_price(symbol, data['Price'])
            return response_pattern(202, "the price has changed", None)
    return response_pattern(404, "the product was not found", None)

def delete_a_product(symbol:str):
    for obj in get_stock_in_table(symbol):
        if symbol==obj[1]:
            delete_in_stocks_table("symbol", symbol)
            return response_pattern(200, "the stock has been deleted", None)
    return response_pattern(404, "the action was not found in the database", None)

def response_pattern(status:int, message:str, content:dict):
    return {"StatusCode": status, "Message": message, "Content": content}, status