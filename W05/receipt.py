import csv

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
            next(reader)  # Skip header row

            for row in reader:
                key = row[key_column_index]  # Product number
                value = row  # Product details (number, name, price)
                products_dict[key] = value

    except FileNotFoundError:
        print(f"Error: El archivo {filename} no se encuentra en el directorio actual.")
    
    return products_dict

def main():
    # Read products into a dictionary
    products_dict = read_dictionary("products.csv", 0)

    # Check if products were loaded correctly
    if not products_dict:
        print("No se pudieron cargar los productos. Verifique el archivo products.csv.")
        return

    # Print all products (optional for debugging)
    print("All Products")
    print(products_dict)

    # Process the request.csv file
    print("\nRequested Items")
    try:
        with open("request.csv", mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            
            for row in reader:
                product_number = row[0]  # Product number from request.csv
                quantity = int(row[1])   # Quantity of the product
                
                # Look up the product details in the products_dict
                product_details = products_dict.get(product_number)
                if product_details:
                    product_name = product_details[1]  # Product name
                    price = float(product_details[2])  # Product price
                    
                    # Print the item information
                    print(f"{product_name}: {quantity} @ {price:.2f}")
                    
                    # Optionally calculate and print the total for the item
                    total = quantity * price
                    print(f"Total: {total:.2f}")
                else:
                    print(f"Product {product_number} no encontrado en el inventario.")
    except FileNotFoundError:
        print("Error: El archivo request.csv no se encuentra en el directorio actual.")

if __name__ == "__main__":
    main()




