from business.stock_business import *
from dao.stock_db import *
import unittest
from unittest.mock import patch
import json

class TestStocksInDataBase(unittest.TestCase):
    @patch('business.stock_business.get_stocks')
    def test_stocks_in_data_base_when_receive_two_results(self, mock_get_stocks):
        stocks_list = [["Company A", "A", 10], ["Company B", "B", 20]] 
        mock_get_stocks.return_value = stocks_list 
        expected_result = ({
                            "Stock": [
                                {"Name": "Company A", "Symbol": "A", "Price": 10},
                                {"Name": "Company B", "Symbol": "B", "Price": 20}                          
                            ]
                            }, 200)
        result = stocks_in_data_base()
        self.assertEqual(result, expected_result)
        
    @patch('business.stock_business.get_stocks')
    def test_stocks_in_data_base_when_receive_a_result(self, mock_get_stocks):
        stocks_list = [["Company A", "A", 10]]
        mock_get_stocks.return_value = stocks_list 
        expected_result = ({
                            "Stock": [{"Name": "Company A", "Symbol": "A", "Price": 10}]
                            }, 200)
        result = stocks_in_data_base()
        self.assertEqual(result, expected_result)
        
    @patch('business.stock_business.get_stocks')
    def test_stocks_in_data_base_receive_when_receive_empty_result(self, mock_get_stocks):
        stocks_list = []
        mock_get_stocks.return_value = stocks_list 
        expected_result = ({
                            "Stock": []
                            }, 200)
        result = stocks_in_data_base()
        self.assertEqual(result, expected_result)
        
class TestSearchStock(unittest.TestCase):
    @patch('business.stock_business.get_stock_in_table')
    def test_search_stock_when_has_a_result(self, mock_get_stocks_in_table):
        mock_get_stocks_in_table.return_value = [["Company A", "ABCD4", 10]]
        expected_result = ({'Stock': [{'Name': 'Company A', 'Symbol': 'ABCD4', 'Price': 10}]}, 200)
        result = search_stock("ABCD4")
        self.assertEqual(result, expected_result)
        
    @patch('business.stock_business.get_stock_in_table')
    def test_search_stock_when_has_not_a_result(self, mock_get_stocks_in_table):
        mock_get_stocks_in_table.return_value = []
        expected_result = ({'Stock': None}, 400)
        result = search_stock("ABCD4")
        self.assertEqual(result, expected_result)
        
    @patch('business.stock_business.get_stock_in_table')
    def test_search_stock_when_has_tree_result(self, mock_get_stocks_in_table):
        mock_get_stocks_in_table.return_value = [["Company A", "ABCD4", 10], ["Company C", "ABCD8", 15], ["Company A", "ABCD4", 10]]
        expected_result = ({'Stock': [{'Name': 'Company A', 'Symbol': 'ABCD4', 'Price': 10}]}, 200)
        result = search_stock("ABCD4")
        self.assertEqual(result, expected_result)
        
    @patch('business.stock_business.get_stock_in_table')
    def test_search_stock_and_the_returned_value_is_the_last_result(self, mock_get_stocks_in_table):
        mock_get_stocks_in_table.return_value = [["Company A", "ABCD4", 10], ["Company C", "CDEF3", 18], ["Company B", "BCDE3", 10]]
        expected_result = ({'Stock': [{'Name': 'Company A', 'Symbol': 'ABCD4', 'Price': 10}]}, 200)
        result = search_stock("ABCD4")
        self.assertEqual(result, expected_result)
        
class TestNewStock(unittest.TestCase): 
    @patch('business.stock_business.insert_in_stocks_table')
    def test_new_stock_fail_integration_test(self, mock_insert_in_stocks_table):
        mock_insert_in_stocks_table.return_value = None
        data = json.loads('{"Name": "CSN MINERACAO", "Symbol": "CMIN3", "Price": 2.53}')
        expected_result = "", 409
        result = new_stock(data)
        self.assertEqual(result, expected_result)
    
    @patch('business.stock_business.insert_in_stocks_table')
    def test_new_stock_sucess_integration_test(self, mock_insert_in_stocks_table):
        mock_insert_in_stocks_table.return_value = None
        data = json.loads('{"Name": "Test", "Symbol": "TSTA4", "Price": 10}')
        expected_result = "", 201
        result = new_stock(data)
        self.assertEqual(result, expected_result)
        
    @patch('business.stock_business.get_stock_in_table')
    @patch('business.stock_business.insert_in_stocks_table')
    def test_new_stock_fail_unit_test(self, mock_insert_in_stocks_table, mock_get_stock_in_table):
        mock_insert_in_stocks_table.return_value = None
        mock_get_stock_in_table.return_value = [["CSN MINERACAO TEST", "CMIN3", 66.66]]
        data = json.loads('{"Name": "CSN MINERACAO", "Symbol": "CMIN3", "Price": 2.53}')
        expected_result = "", 409
        result = new_stock(data)
        self.assertEqual(result, expected_result)
    
    @patch('business.stock_business.get_stock_in_table')
    @patch('business.stock_business.insert_in_stocks_table')
    def test_new_stock_sucess_unit_test(self, mock_insert_in_stocks_table, mock_get_stock_in_table):
        mock_insert_in_stocks_table.return_value = None
        mock_get_stock_in_table.return_value = []
        data = json.loads('{"Name": "Test", "Symbol": "TSTA4", "Price": 10}')
        expected_result = "", 201
        result = new_stock(data)
        self.assertEqual(result, expected_result)
    
class TestChangeStockPrice(unittest.TestCase):
    @patch('business.stock_business.get_stock_in_table')
    @patch('business.stock_business.update_price')
    def test_change_stock_price_sucess(self, mock_update_price,  mock_get_stock_in_table):
        mock_update_price.return_value = None
        mock_get_stock_in_table.return_value = [["CSN MINERACAO TEST", "CMIN3", 77.77]]
        data = json.loads('{"Price": 10.03}')
        expected_result = "", 202
        result = change_stock_price("CMIN3", data)
        self.assertEqual(result, expected_result)
    
    @patch('business.stock_business.get_stock_in_table')
    @patch('business.stock_business.update_price')
    def test_change_stock_price_fail(self, mock_update_price, mock_get_stock_in_table):
        mock_get_stock_in_table.return_value = []
        mock_update_price.return_value = None
        data = json.loads('{"Price": 10.03}')
        expected_result = "", 404
        result = change_stock_price("TEST8", data)
        self.assertEqual(result, expected_result)

class TestDeleteAProduct(unittest.TestCase):
    @patch('business.stock_business.get_stock_in_table')
    @patch('business.stock_business.delete_in_stocks_table')
    def test_delete_a_product_sucess(self, mock_delete_in_stocks_table, mock_get_stock_in_table):
        mock_get_stock_in_table.return_value = [["CSN MINERACAO TEST", "CMIN3", 9.99]]
        mock_delete_in_stocks_table.return_value = None
        expected_result = "", 200
        result = delete_a_product("CMIN3")
        self.assertEqual(result, expected_result)
        
    @patch('business.stock_business.get_stock_in_table')
    @patch('business.stock_business.delete_in_stocks_table')
    def test_delete_a_product_fail(self, mock_delete_in_stocks_table, mock_get_stock_in_table):
        mock_get_stock_in_table.return_value = []
        mock_delete_in_stocks_table.return_value = None
        expected_result = "", 404
        result = delete_a_product("CMIN4")
        self.assertEqual(result, expected_result)
        