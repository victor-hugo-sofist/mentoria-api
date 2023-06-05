from flask import Flask
from business.stock_business import *

app = Flask(__name__, template_folder='C:\\projeto\\new-mentoria-api\\app\controller\\views')

@app.route('/', methods = ['GET'])
def home():
    return home_page()

@app.route('/download/', methods = ['GET'])
def download():
    response = collection()
    return jsonify(response)

@app.route('/stocks/', methods = ['GET'])
def show_stocks_in_data_base():
    response, code = stocks_in_data_base()
    return jsonify(response), code

@app.route('/stock/<symbol>/', methods = ['GET'])
def show_search_stock(symbol):
    response, code = search_stock(symbol)
    return jsonify(response), code

@app.route('/new/stock/', methods = ['POST'])
def post_new_stock():
    data = json.loads(request.data)
    response, code = new_stock(data)
    return jsonify(response), code

@app.route('/stock/<symbol>/change/price/', methods = ['PATCH'])
def patch_change_stock_price(symbol:str):
    data = json.loads(request.data)
    response, code = change_stock_price(symbol, data)
    return jsonify(response), code

@app.route('/stock/delete/<symbol>/', methods = ['DELETE'])
def delete_product(symbol:str):
    response, code = delete_a_product(symbol)
    return jsonify(response), code

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)


