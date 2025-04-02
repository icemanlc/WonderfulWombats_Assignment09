# File Name : description.py
# Student Name: Saivamsi Amireddy
# email:  amiredsr@mail.uc.edu
# Assignment Number: Assignment 09
# Due Date:   April 03, 2025
# Course #/Section:   IS 4010 Section 001
# Semester/Year:   Spring 2025
# Brief Description of the assignment:  We extract data from the Grocery Store Simulator database in a SQL Server and run queries to explore the data.
# Brief Description of what this module does: It uses previously queried data to create a sales report sentence.

import pyodbc

class ProductAnalytics:     
    def __init__(self):
        self.conn = pyodbc.connect(
            'Driver={SQL Server};'
            'Server=lcb-sql.uccob.uc.edu\\nicholdw;'
            'Database=GroceryStoreSimulator;'
            'uid=IS4010Login;'
            'pwd=P@ssword2;'
        )
        self.cursor = self.conn.cursor()
        self.product_id = None
        self.description = None
        self.manufacturer_id = None
        self.brand_id = None
        self.manufacturer_name = None
        self.brand_name = None
        self.number_of_items_sold = 0

    def get_items_sold(self, product_id):
            """
            Get the number of items sold for a specific product.
            Implements step 6 of the assignment.
        
            @param product_id: The ID of the product to analyze
            @return: The number of items sold as an integer
            """
            cursor = self.conn.cursor()
            query = """
                SELECT TOP (100) PERCENT SUM(dbo.tTransactionDetail.QtyOfProduct) AS NumberOfItemsSold
                FROM dbo.tTransactionDetail INNER JOIN
                dbo.tTransaction ON dbo.tTransactionDetail.TransactionID = dbo.tTransaction.TransactionID 
                WHERE (dbo.tTransaction.TransactionTypeID = 1) AND (dbo.tTransactionDetail.ProductID = ?)
            """
            cursor.execute(query, (product_id,))
            result = cursor.fetchone()
        
            # Return 0 if no sales data is found
            return result[0] if result and result[0] is not None else 0
    
    def create_sales_report(self, product_description, manufacturer_name, brand_name, items_sold):
        """
        Create a grammatically correct sentence reporting sales information.
        Implements step 7 of the assignment.
        
        @param product_description: Description of the product
        @param manufacturer_name: Name of the manufacturer
        @param brand_name: Name of the brand
        @param items_sold: Number of items sold
        @return: A formatted string containing the sales report
        """
        return f"The product '{product_description}', manufactured by {manufacturer_name} under the {brand_name} brand, has sold {items_sold} units."

   

    def close_connection(self):
        """
        Closes the database connection.
        """
        self.cursor.close()
        self.conn.close()