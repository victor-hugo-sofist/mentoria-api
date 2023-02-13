from flask import Flask
from business.stock_business import *

app = Flask(__name__, template_folder='C:\\projeto\\new-mentoria-api\\app\controller\\views')

@app.route('/', methods = ['GET'])
def home():
    # exemple_hello()
    return home_page()

@app.route('/download/', methods = ['GET'])
def download():
    return collection()

@app.route('/stocks/', methods = ['GET'])
def show_stocks_in_data_base():
    return stocks_in_data_base()

@app.route('/stock/<symbol>/', methods = ['GET'])
def show_search_stock(symbol):
    return search_stock(symbol)

@app.route('/new/stock/', methods = ['POST'])
def post_new_stock():
    return new_stock()

@app.route('/stock/<symbol>/change/price/', methods = ['PATCH'])
def patch_change_stock_price(symbol:str):
    return change_stock_price(symbol)

@app.route('/stock/delete/<symbol>/', methods = ['DELETE'])
def delete_product(symbol:str):
    return delete_a_product(symbol)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)


