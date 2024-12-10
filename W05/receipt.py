import csv
from datetime import datetime

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.
    
    Parameters:
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    
    Return:
        A compound dictionary that contains the contents of the CSV file.
    """
    products_dict = {}

    try:
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                key = row[key_column_index] 
                value = row 
                products_dict[key] = value

    except FileNotFoundError:
        print(f"Error: The file {filename} was not found in the current directory.")
        return {}
    
    return products_dict

def main():
    products_dict = read_dictionary("products.csv", 0)

    if not products_dict:
        print("Failed to load products. Please check the products.csv file.")
        return

    print("All Products")
    print(products_dict)

    subtotal = 0

    print("\nRequested Items")
    try:
        with open("request.csv", mode='r') as file:
            reader = csv.reader(file)
            next(reader)  
            
            for row in reader:
                product_number = row[0]  
                quantity = int(row[1])   

                product_details = products_dict.get(product_number)
                if product_details:
                    product_name = product_details[1] 
                    price = float(product_details[2])  

                    total = quantity * price
                    subtotal += total
                    print(f"{product_name}: {quantity} @ {price:.2f}")
                    print(f"Total: {total:.2f}")
                else:
                    print(f"Product {product_number} not found in the inventory.")
    except FileNotFoundError:
        print("Error: The file request.csv was not found in the current directory.")
        return

    sales_tax = subtotal * 0.06
    grand_total = subtotal + sales_tax

    print("\nReceipt Summary")
    print(f"Subtotal: {subtotal:.2f}")
    print(f"Sales Tax (6%): {sales_tax:.2f}")
    print(f"Grand Total: {grand_total:.2f}")

    print(f"\nDate and Time: {datetime.now():%A, %B %d, %Y %I:%M %p}")
    print("Thank you for shopping with us!")

if __name__ == "__main__":
    main()