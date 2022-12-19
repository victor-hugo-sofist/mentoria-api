from flask import Flask, jsonify, request, json, render_template
from src.stock import Stock
from colection import download

banco_de_dados = []
banco_de_dados.append(Stock("CSN MINERACAO", "CMIN3", 2.5))
banco_de_dados.append(Stock("ITAU", "ITUB4", 26.5))
banco_de_dados.append(Stock("VALE", "VALE3", 20.5))
banco_de_dados.append(Stock("MAXI RENDA", "MXRF11", 10.5))

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def home_page():
    return render_template("home_page.html")

@app.route('/download/', methods = ['GET'])
def collection():
    return download

@app.route('/stocks/', methods = ['GET'])
def stocks_in_data_base():
    response = []
    for obj in banco_de_dados:
        response.append({
                        "Name": obj.stock_name,
                        "Symbol": obj.stock_symbol,
                        "Price": obj.price
                        })
    stocks = {"Stocks": response}
    return jsonify(stocks), 200

@app.route('/stock/<symbol>/', methods = ['GET'])
def search_stock(symbol):
    response = []
    for obj in banco_de_dados:
        if symbol==obj.stock_symbol:
            response.append({
                            "Name": obj.stock_name,
                            "Symbol": obj.stock_symbol,
                            "Price": obj.price
                            })
            stock = {"Stock": response}
            return jsonify(stock), 200   
    stock = {"Stock": None}
    return jsonify(stock), 400

@app.route('/new/stock/', methods = ['POST'])
def new_stock():
    data = json.loads(request.data)
    banco_de_dados.append(
                        Stock(data['Name'],
                        data['Symbol'],
                        data['Price'],
                        ))
    return "", 201

@app.route('/stock/<symbol>/change/price/', methods = ['PATCH'])
def change_stock_price(symbol:str):
    data = json.loads(request.data)
    for obj in banco_de_dados:
        if symbol==obj.stock_symbol:
            obj.update_price(data['Price'])
            return "", 202
    return "", 404

@app.route('/stock/delete/<symbol>/', methods = ['DELETE'])
def delete_product(symbol:str):
    for obj in banco_de_dados:
        if symbol==obj.stock_symbol:
            banco_de_dados.remove(obj)
            return "", 200
    return "", 404

app.run(host='0.0.0.0', debug=True)
