# File Name : Random.py
# Student Name: Lucas Iceman
# email:  icemanlc@mail.uc.edu
# Assignment Number: Assignment 09
# Due Date:   4/3/2025
# Course #/Section:   IS4010-001
# Semester/Year:   Spring 2025
# Brief Description of the assignment:We extract data from the Grocery Store Simulator database in a SQL Server and run queries to explore the data.
# Brief Description of what this module does: this moduale Randomly select one row from the data structure from the query. 
# Citations: N/A
# Anything else that's relevant:N/A

import pyodbc
import random

class ProductSelector:
    def __init__(self):
        self.selected_product = None
        self.description = None
        self.product_id = None
        self.manufacturer_id = None
        self.brand_id = None

    def connect_to_database(self):
        """
        Connect to our SQL Server instance
        @return connection object
        """
        conn = pyodbc.connect(
            'Driver={SQL Server};'
            'Server=lcb-sql.uccob.uc.edu\\nicholdw;'
            'Database=GroceryStoreSimulator;'
            'uid=IS4010Login;'
            'pwd=P@ssword2;'
        )
        return conn

    def load_and_select_product(self):
        """
        Run SQL statement and store a random instence 
        @return No products found
        """
        conn = self.connect_to_database()
        cursor = conn.cursor()
        cursor.execute('SELECT ProductID, [UPC-A ], Description, ManufacturerID, BrandID FROM tProduct')
        rows = cursor.fetchall()

        columns = [column[0] for column in cursor.description]
        conn.close()

        if rows:
            selected_row = random.choice(rows)
            row_dict = dict(zip(columns, selected_row))

            self.selected_product = row_dict
            self.product_id = row_dict['ProductID']
            self.description = row_dict['Description']
            self.manufacturer_id = row_dict['ManufacturerID']
            self.brand_id = row_dict['BrandID']
        else:
            print("No products found.")
