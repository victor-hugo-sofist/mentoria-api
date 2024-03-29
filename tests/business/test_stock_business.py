import unittest
from app.business.stock_business import *
from app.dao.stock_db import *
from unittest.mock import patch
import json

class TestStocksInDataBase(unittest.TestCase):
    @patch('app.business.stock_business.get_stocks')
    def test_stocks_in_data_base_when_receive_two_results(self, mock_get_stocks):
        stocks_list = [["Company A", "A", 10], ["Company B", "B", 20]] 
        mock_get_stocks.return_value = stocks_list 
        expected_result = ({"Content": {
                            "Stocks": [
                                {"Name": "Company A", "Symbol": "A", "Price": 10},
                                {"Name": "Company B", "Symbol": "B", "Price": 20}                          
                            ]
                            }, "Message": "there are stocks in the database", 
                            "StatusCode": 200
                            }, 200)   
        result = stocks_in_data_base()
        self.assertEqual(result, expected_result)
        
    @patch('app.business.stock_business.get_stocks')
    def test_stocks_in_data_base_when_receive_a_result(self, mock_get_stocks):
        stocks_list = [["Company A", "A", 10]]
        mock_get_stocks.return_value = stocks_list     
        expected_result = ({"Content": {
                            "Stocks": [
                                {"Name": "Company A", "Symbol": "A", "Price": 10}]
                            }, "Message": "there are stocks in the database", 
                            "StatusCode": 200
                            }, 200) 
        result = stocks_in_data_base()
        self.assertEqual(result, expected_result)
        
    @patch('app.business.stock_business.get_stocks')
    def test_stocks_in_data_base_receive_when_receive_empty_result(self, mock_get_stocks):
        stocks_list = []
        mock_get_stocks.return_value = stocks_list       
        expected_result = ({"Content": {
                            "Stocks": []
                            }, "Message": "there are NOT stocks in the database", 
                            "StatusCode": 404
                            }, 404)
        result = stocks_in_data_base()
        self.assertEqual(result, expected_result)
        
class TestSearchStock(unittest.TestCase):
    @patch('app.business.stock_business.get_stock_in_table')
    def test_search_stock_when_has_a_result(self, mock_get_stocks_in_table):
        mock_get_stocks_in_table.return_value = [["Company A", "ABCD4", 10]]
        expected_result = ({"Content": {
                            "Stock": [{'Name': 'Company A', 'Symbol': 'ABCD4', 'Price': 10}]},
                            "Message": "there are a stock with symbol ABCD4 in database", 
                            "StatusCode": 200
                            }, 200)
        result = search_stock("ABCD4")
        self.assertEqual(result, expected_result)
        
    @patch('app.business.stock_business.get_stock_in_table')
    def test_search_stock_when_has_not_a_result(self, mock_get_stocks_in_table):
        mock_get_stocks_in_table.return_value = []
        expected_result = ({"Content": None,
                            "Message": "there are NOT a stock with this symbol in database", 
                            "StatusCode": 400
                            }, 400)
        result = search_stock("ABCD4")
        self.assertEqual(result, expected_result)
        
    @patch('app.business.stock_business.get_stock_in_table')
    def test_search_stock_when_has_tree_result(self, mock_get_stocks_in_table):
        mock_get_stocks_in_table.return_value = [["Company A", "ABCD4", 10], ["Company C", "ABCD8", 15], ["Company E", "EBCD4", 1]]
        expected_result = ({"Content": {
                            "Stock": [{'Name': 'Company E', 'Symbol': 'EBCD4', 'Price': 1}]},
                            "Message": "there are a stock with symbol EBCD4 in database", 
                            "StatusCode": 200
                            }, 200)
        result = search_stock("EBCD4")
        self.assertEqual(result, expected_result)
        
    @patch('app.business.stock_business.get_stock_in_table')
    def test_search_stock_and_the_returned_value_is_the_first_result(self, mock_get_stocks_in_table):
        mock_get_stocks_in_table.return_value = [["Company A", "ABCD4", 10], ["Company C", "CDEF3", 18], ["Company B", "BCDE3", 10]]
        expected_result = ({"Content": {
                            "Stock": [{'Name': 'Company A', 'Symbol': 'ABCD4', 'Price': 10}]},
                            "Message": "there are a stock with symbol ABCD4 in database", 
                            "StatusCode": 200
                            }, 200)
        result = search_stock("ABCD4")
        self.assertEqual(result, expected_result)
        
class TestNewStock(unittest.TestCase): 
    @patch('app.business.stock_business.insert_in_stocks_table')
    def test_new_stock_fail_integration_test_when_trying_to_register_an_existing_stock(self, mock_insert_in_stocks_table):
        mock_insert_in_stocks_table.return_value = None
        data = json.loads('{"Name": "CSN MINERACAO", "Symbol": "CMIN3", "Price": 2.53}')
        expected_result = ({
                            "StatusCode": 409,
                            "Message": "it was not possible to create a new action because the symbol is already in use",
                            "Content": None
                        }, 409)
        result = new_stock(data)
        self.assertEqual(result, expected_result)
    
    @patch('app.business.stock_business.insert_in_stocks_table')
    def test_new_stock_sucess_integration_test_when_trying_to_register_a_new_stock(self, mock_insert_in_stocks_table):
        mock_insert_in_stocks_table.return_value = None
        data = json.loads('{"Name": "Test", "Symbol": "TSTA4", "Price": 10}')
        expected_result = ({
                "StatusCode": 201,
                "Message": "new stock created",
                "Content": None
                }, 201)
        result = new_stock(data)
        self.assertEqual(result, expected_result)
        
    @patch('app.business.stock_business.get_stock_in_table')
    @patch('app.business.stock_business.insert_in_stocks_table')
    def test_new_stock_when_trying_to_register_an_existing_stock(self, mock_insert_in_stocks_table, mock_get_stock_in_table):
        mock_insert_in_stocks_table.return_value = None
        mock_get_stock_in_table.return_value = [["CSN MINERACAO TEST", "CMIN3", 66.66]]
        data = json.loads('{"Name": "CSN MINERACAO", "Symbol": "CMIN3", "Price": 2.53}')
        expected_result = ({
                "StatusCode": 409,
                "Message": "it was not possible to create a new action because the symbol is already in use",
                "Content": None
                }, 409)
        result = new_stock(data)
        self.assertEqual(result, expected_result)
    
    @patch('app.business.stock_business.get_stock_in_table')
    @patch('app.business.stock_business.insert_in_stocks_table')
    def test_new_stock_when_trying_to_register_a_new_stock(self, mock_insert_in_stocks_table, mock_get_stock_in_table):
        mock_insert_in_stocks_table.return_value = None
        mock_get_stock_in_table.return_value = []
        data = json.loads('{"Name": "Test", "Symbol": "TSTA4", "Price": 10}')
        expected_result = ({
                "StatusCode": 201,
                "Message": "new stock created",
                "Content": None,
                }, 201)
        result = new_stock(data)
        self.assertEqual(result, expected_result)
    
class TestChangeStockPrice(unittest.TestCase):
    @patch('app.business.stock_business.get_stock_in_table')
    @patch('app.business.stock_business.update_price')
    def test_change_stock_price_of_an_existing_product(self, mock_update_price,  mock_get_stock_in_table):
        mock_update_price.return_value = None
        mock_get_stock_in_table.return_value = [["CSN MINERACAO TEST", "CMIN3", 77.77]]
        data = json.loads('{"Price": 10.03}')
        expected_result = ({
                "StatusCode": 202,
                "Message": "the price has changed",
                "Content": None,
                }, 202)
        result = change_stock_price("CMIN3", data)
        self.assertEqual(result, expected_result)
    
    @patch('app.business.stock_business.get_stock_in_table')
    @patch('app.business.stock_business.update_price')
    def test_change_stock_price_of_a_non_existent_product(self, mock_update_price, mock_get_stock_in_table):
        mock_get_stock_in_table.return_value = []
        mock_update_price.return_value = None
        data = json.loads('{"Price": 10.03}')
        expected_result = ({
                "StatusCode": 404,
                "Message": "the product was not found",
                "Content": None,
                }, 404)
        result = change_stock_price("TEST8", data)
        self.assertEqual(result, expected_result)

class TestDeleteAProduct(unittest.TestCase):
    @patch('app.business.stock_business.get_stock_in_table')
    @patch('app.business.stock_business.delete_in_stocks_table')
    def test_delete_a_product_of_an_existing_product(self, mock_delete_in_stocks_table, mock_get_stock_in_table):
        mock_get_stock_in_table.return_value = [["CSN MINERACAO TEST", "CMIN3", 9.99]]
        mock_delete_in_stocks_table.return_value = None
        expected_result = ({
                "StatusCode": 200,
                "Message": "the stock has been deleted",
                "Content": None,
                }, 200)
        result = delete_a_product("CMIN3")
        self.assertEqual(result, expected_result)
        
    @patch('app.business.stock_business.get_stock_in_table')
    @patch('app.business.stock_business.delete_in_stocks_table')
    def test_delete_a_product_of_a_non_existent_product(self, mock_delete_in_stocks_table, mock_get_stock_in_table):
        mock_get_stock_in_table.return_value = []
        mock_delete_in_stocks_table.return_value = None
        expected_result = "", 404
        expected_result = ({
                "StatusCode": 404,
                "Message": "the action was not found in the database",
                "Content": None,
                }, 404)
        result = delete_a_product("CMIN4")
        self.assertEqual(result, expected_result)