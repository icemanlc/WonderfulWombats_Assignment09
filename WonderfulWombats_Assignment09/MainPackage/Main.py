# Main.py
# File Name : Main.py
# Student Name: Lucas Iceman, Zulqarnayan Hossain, Saivamsi Reddy Amireddy
# email:  icemanlc@mail.uc.edu, hossaizn@mail.uc.edu, amiredsr@mail.uc.edu
# Assignment Number: Assignment 09
# Due Date:   April 03, 2025
# Course #/Section:   IS 4010 Section 001
# Semester/Year:   Spring 2025
# Brief Description of the assignment:  We extract data from the Grocery Store Simulator database in a SQL Server and run queries to explore the data.
# Brief Description of what this module does. We work on connecting to external data sources and retrieving information to explore data using python.
# Citations: N/A
# Anything else that's relevant: N/A

 
from LIPackage.random import *
from ZHPackage.lookup import *
from SAPackage.description import *


def main():


    #Lucas Section 

    selector = ProductSelector()
    selector.load_and_select_product()
    """
    print("Randomly selected product:")
    print(f"Description: {selector.description}")
    print(f"Product ID: {selector.product_id}")
    print(f"Manufacturer ID: {selector.manufacturer_id}")
    print(f"Brand ID: {selector.brand_id}")
    """

    #End Lucas Section

    #Start Zulqarnayan Section

    lookup = Lookup()

    manufacturer_name = lookup.find_manufacturer_name(selector.manufacturer_id)
    brand_name = lookup.find_brand_name(selector.brand_id)
    """
    print(f"Manufacturer name: {manufacturer_name}")
    print(f"Brand name: {brand_name}")
    """
    #End Zulqarnayan Section

    #Start Saivamsi Section

    analytics = ProductAnalytics() 
    
    items_sold = analytics.get_items_sold(selector.product_id)
    output_sentence = analytics.create_sales_report(
        selector.description,
        manufacturer_name,
        brand_name,
        items_sold
    )
    print(output_sentence)
    analytics.close_connection() 

    #End Saivamsi Section


if __name__ == "__main__":
    main()
























#End Saivansi Section

#start Zulqarnayan Section



































#end Zulqarnayan Section