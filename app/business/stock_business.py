from flask import jsonify, request, json, render_template
from dao.stock_db import *
from postman.collection import download

def home_page():
    return render_template("home_page.html")

def collection():
    return download

#fazer testes unitários deste item
def stocks_in_data_base():
    response = []
    for obj in get_stocks():
        response.append({
                            "Name": obj[0],
                            "Symbol": obj[1],
                            "Price": obj[2]
                        })
        stocks = {"Stock": response}
    return jsonify(stocks), 200  

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
            return jsonify(stock), 200
    stock = {"Stock": None}
    return jsonify(stock), 400

def new_stock():
    data = json.loads(request.data)
    for obj in get_stock_in_table(data['Symbol']):
        if len(obj) > 0:
            return "", 409
    insert_in_stocks_table(Stock(data['Name'], data['Symbol'], data['Price']))
    return "", 201


def change_stock_price(symbol:str):
    data = json.loads(request.data)
    for obj in get_stock_in_table(symbol):
        if symbol==obj[1]:
            update_price(symbol, data['Price'])
            return "", 202
    return "", 404

def delete_a_product(symbol:str):
    for obj in get_stock_in_table(symbol):
        if symbol==obj[1]:
            delete_in_stocks_table("symbol", symbol)
            return "", 200
    return "", 404