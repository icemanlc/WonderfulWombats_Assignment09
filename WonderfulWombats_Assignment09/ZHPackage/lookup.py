# Zulqarnayan's module
# File Name : lookup.py
# Student Name: Zulqarnayan Hossain
# email:  hossaizn@mail.uc.edu
# Assignment Number: Assignment 09
# Due Date:   April 03, 2025
# Course #/Section:   IS 4010 Section 001
# Semester/Year:   Spring 2025
# Brief Description of the assignment:  We extract data from the Grocery Store Simulator database in a SQL Server and run queries to explore the data.

# Brief Description of what this module does. We work on connecting to external data sources and retrieving information to explore data using python.
# Citations: N/A

# Anything else that's relevant: N/A

import pyodbc

class Lookup:
    def __init__(self):
        self.conn = pyodbc.connect(
            'Driver={SQL Server};'
            'Server=lcb-sql.uccob.uc.edu\\nicholdw;'
            'Database=GroceryStoreSimulator;'
            'uid=IS4010Login;'
            'pwd=P@ssword2;'
        )

    def find_manufacturer_name(self, manufacturer_id):
        """
        Find the manufacturer name by its ID.
        @return Manufacturer name as a string or None if not found.
        """
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT Manufacturer FROM tManufacturer WHERE ManufacturerID = ?",
            (manufacturer_id,)
        )
        result = cursor.fetchone()
        return result[0] if result else None

    def find_brand_name(self, brand_id):
        """
        Find the brand name by its ID.
        @return Brand name as a string or None if not found.
        """
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT Brand FROM tBrand WHERE BrandID = ?",
            (brand_id,)
        )
        result = cursor.fetchone()
        return result[0] if result else None




     