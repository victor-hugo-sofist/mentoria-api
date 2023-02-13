import sqlite3

class Db_sqlite:
    def __init__(self):
        self.conn = sqlite3.connect('my_db_sqlite.db')
        self.cursor = self.conn.cursor()

    def save_and_close(self):
        self.conn.commit()
        self.close()
    
    def close(self):
        self.conn.close()
    
    def insert(self, table:str, value:str):
        cmd = "INSERT INTO " + table + " VALUES " + value
        self.cursor.execute(cmd)
        self.save_and_close()

    def delete(self, table:str, column:str, data): #OK
        operation = False
        if type(data) == int or type(data) == float:
            cmd = "DELETE FROM " + table + " WHERE " + column + " = " + str(data)
            self.cursor.execute(cmd)
            operation = True
        if type(data) == str:
            cmd = "DELETE FROM " + table + " WHERE " + column + " = '" + data + "'"
            self.cursor.execute(cmd)
            operation = True
        if operation == True:
            self.save_and_close()
        else:
            self.close()
    
    def __delete_table(self, table:str):
        cmd = "DELETE FROM " + table
        self.cursor.execute(cmd)
        self.save_and_close()

    def get_selected_table(self, table:str): 
        cmd = "SELECT * FROM " + table
        self.cursor.execute(cmd)
        rows = self.cursor.fetchall()
        self.close()
        return rows
        

    def get_select_table_data(self, table:str, columns:str, conditions:str):
        cmd = "SELECT * FROM " + table +" WHERE "+ columns + " LIKE " + "'" + conditions+ "'"
        self.cursor.execute(cmd)
        rows = self.cursor.fetchall()
        self.close()
        return rows

    def update_value(self, table:str, search_data_column:str, search_data:str, new_value_columns:str, new_value:str):
        cmd = "UPDATE " + table + " SET " + new_value_columns + " = " + new_value + " WHERE " + search_data_column + " = " + search_data
        self.cursor.execute(cmd)
        self.save_and_close()
        