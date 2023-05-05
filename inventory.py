#========Import Modules==========
from tabulate import tabulate

#========The beginning of the class==========
class Shoe:

    # inititialise the following attributes in the class: country, code, product, cost, quantity
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    # Define method to return the shoe cost   
    def get_cost(self):
        shoe_cost = self.cost
        return shoe_cost

   # Define method to return the quanity of shoes
    def get_quantity(self):
        shoe_quanity = self.quantity
        return shoe_quanity

    # Define a method that returns a string representation of a class
    def __str__(self):
        return f"{self.country},{self.code},{self.product},{self.cost},{self.quantity}"

# Create a subclass that inherents the attributes and functions from the parent Shoe class
# Use super function when intitialising the attributes in order to inherent the parent attributes
# and methods.
class Shoe_Value(Shoe):
    def __init__(self, country, code, product, cost, quantity, value):
        super().__init__(country, code, product, cost, quantity)
        self.value = value

    def __str__(self):
        return f"{self.country},{self.code},{self.product},{self.cost},{self.quantity},{self.value}"


#=============Shoe list===========

# Create a list that will be used to store a list of objects of shoes
shoe_list = []

#==========Functions outside the class==============

def read_shoes_data():

# Define function that will open the inventory.txt file and read data from the file
# Skip reading the the first line of the txt file by using the next() function
# Create a shoes object with the data and append the object into the shoe list

    # If there is no inventory file, create a new file for inventory using try/except
      
    if len(shoe_list) == 0:
        try:
            with open("inventory.txt", "r") as file:

                next(file)

                for lines in file:
                    temp = lines.strip()
                    temp = temp.split(",")

                    shoe_object = Shoe(temp[0], temp[1], temp[2], temp[3], temp[4])                      
                    shoe_list.append(shoe_object)
        
        except FileNotFoundError:
            with open("inventory.txt", "w") as file:
                file.write("Country,Code,Product,Cost,Quantity")

        return shoe_list

def capture_shoes(country, code, product, cost, quantity):
# Define function that emables user to capture data about the shoe
# Use the the data to create a shoe object
# Append this object to inside the shoe list

    shoe_object = Shoe(country, code, product, cost, quantity)
    shoe_list.append(shoe_object)
    return shoe_object.__str__()


def view_all():
# Define function to iterate over the shoes list
# and print the details of the shoes retured from the __str__ function
# and append those into a shoe list that displays the shoe attribute details in the list
# Organise the data in a table format by using Python's tabulate module

    shoe_list_attribute_detail_list = []

    for shoe_object in shoe_list:
        shoe_details = shoe_object.__str__().split(",")
        shoe_list_attribute_detail_list.append(shoe_details)

    print("The following is all of the shoe inventory on hand:")
    inventory_table = tabulate(shoe_list_attribute_detail_list, headers= ["Country", "Code", "Product", "Cost", "Quantity"])
    print(inventory_table)


def re_stock():
# Define object that will find the shoe object with the lowest quantity,
# which is the shoe that will need to be restocked.
# Request the user if they would like to add this quantity of shoes and then update it.
# This quantity should be updated on the file for this shoe

    temp_quantity_list = []

    # Convert stock quantity to integers and append the integers in a tempory list of stock quantities
    # identify the minimum quantity in the temporary quantity list
    for shoe_object in shoe_list:
        quanity_converted_integers = int(shoe_object.quantity)
        temp_quantity_list.append(quanity_converted_integers)
        min_quantity = min(temp_quantity_list)

    # If the stock quantity matches the minimum quantity identified above,
    # create a temporary nested list that will store objects that have the minimum quanity identified, with the attribute details listed.
    # Format the items this relates to in a table using the tabulate module and print out the items this minimum relates to.
    min_shoe_list_attribute_detail_list = []

    for shoe_object in shoe_list:
        if shoe_object.quantity == str(min_quantity):
        # and shoe_list.count(shoe_object) == 1:
            shoe_details = shoe_object.__str__().split(",")

            if shoe_details not in min_shoe_list_attribute_detail_list:
                min_shoe_list_attribute_detail_list.append(shoe_details)

    inventory_table = tabulate(min_shoe_list_attribute_detail_list, headers= ["Country", "Code", "Product", "Cost", "Quantity"])
    print(f"The stock with the lowest quanity is the following: \n {inventory_table}")
    
    # In case there is more than 1 item returns with the minimum stock, create a for loop so the user can evaluate every item
    # that has the minimum quanity to determine if they would like to update the respective quanity
    # Request user to indicate if they would like to add to the quanity of the shoe item dispalyed as having with the minimum/lowest quantity
    for index in range(len(min_shoe_list_attribute_detail_list)):
        SKU_code_shoe =  min_shoe_list_attribute_detail_list[index][1]
        Product = min_shoe_list_attribute_detail_list[index][2]
        user_update_query = input(f"Would you like to add to the quantity of shoes for {SKU_code_shoe}- {Product} (Yes/No): ")

        # If user selects to add to the quantity, request user to indicate the additional quantity they would like to add
        # Print out error message if the user attempts to enter a value that is not an integer or is less than 0 and request to try again.
        if user_update_query.lower() == "yes":
            while True:
                try:
                    add_stock = int(input(f"Enter how much additional stock you would like to add to {SKU_code_shoe}- {Product} (i.e. additional quantity to be added for the restock):"))
                    if add_stock >= 0:
                        break
                    else:
                        print("Error: Invalid value. The stock to be added cannot be a negative integer. Please try again.")
                except ValueError:
                    print("Error: Invalid value. The entry should be an integer. Please try again.")
            
            # Update inventory for the quantity of stock the user would like to add
            # Create a temporary nested list that will store objects that show the updated quanities after restocking, with the attribute details listed
            # Print out the new total inventory quantity balance in a table, with the related stock information.

            temp_shoe_list_updated_quantities = []  
            
            for shoe_object in shoe_list:      
                if shoe_object.quantity == str(min_quantity) and shoe_object.code == SKU_code_shoe:
                    new_quantity = int(shoe_object.quantity) + add_stock
                    shoe_object.quantity = new_quantity
                    shoe_details = shoe_object.__str__().split(",")

                    if shoe_details not in temp_shoe_list_updated_quantities:
                        temp_shoe_list_updated_quantities.append(shoe_details)
                
            inventory_table = tabulate(temp_shoe_list_updated_quantities , headers= ["Country", "Code", "Product", "Cost", "Quantity"])
            print(f"The updated quantity for the stock is as follows: \n {inventory_table}")
    
            # Update the inventory.txt file with the updated quantities
            with open("inventory.txt", "w") as file:
                file.write("Country,Code,Product,Cost,Quantity\n")
                for shoe_object in shoe_list:
                    file.write(f"{shoe_object.__str__()}\n")
                print("Done- Inventory list updated")
        
        elif user_update_query.lower() == "no":
            print("Noted- no updates will be made to this item.")

        else:
            print("Error: Invalid input. The options available are 'Yes' or 'No'. No updates will be made to this item.")

def search_shoe():
    #Define function that will search for a shoe from the list
    #using the shoe code and return this object so that it will be printed.

    temp_list_code_search = []

    # Print out error message if the code entered is not a valid SKU code and request the user to try again
    while len(temp_list_code_search) == 0:

        search_shoe_code = input("Please enter the code (SKU) of the shoe that you'd like to search: ")

        for shoe_object in shoe_list:
            if shoe_object.code == search_shoe_code:
                shoe_details = shoe_object.__str__().split(",")

                temp_list_code_search = [shoe_details]
                break

        inventory_table = tabulate(temp_list_code_search, headers= ["Country", "Code", "Product", "Cost", "Quantity"])
        print(inventory_table) 

        if len(temp_list_code_search) == 0:
            print("The value that you entered is not a valid SKU code. Please try again or enter 'exit' to leave this menu option.")

        # Enable user to exit this menu item if they enter "exit."
        if search_shoe_code.lower() == "exit":
            break

def value_per_item():
    # Define function that will calculate the total value for each item.
    # where value = cost * quantity.
    # Print this information on the console for all the shoes.

    temp_shoe_list_incl_val = []
    
    # Read from inventory.txt file
    # Cast the cost and quanity of each item and calculate the value of each item
    # Create an object of the Shoe_value class which includes the attribute of value
    # Create a temporary list in order to format the data in a table using the tabulate module
    # Print out all the stock items in a table, including the column for the inventory value
    with open("inventory.txt", "r") as file:

        next(file)

        for lines in file:
            temp = lines.strip()
            temp = temp.split(",")

            # Casting the cost to a float first and then an integer to avoid a ValueError for trying to pass a string with decimals straight to an integer
            value = int(float(temp[3])) * int(temp[4])
        
            shoe_object_incl_val_object = Shoe_Value(temp[0], temp[1], temp[2], temp[3], temp[4],value)

            list_attributes = shoe_object_incl_val_object.__str__().split(",")
            temp_shoe_list_incl_val.append(list_attributes)            

    
    inventory_table = tabulate(temp_shoe_list_incl_val, headers= ["Country", "Code", "Product", "Cost", "Quantity","Inventory Value"])
    print(inventory_table) 

def highest_qty():
    # Define function that determines the product with the highest quantity
    # print out that this shoe(s) shoe is for sale.

    temp_quanity_list = []

    # Convert stock quantity to integers and append the integers in a tempory list of stock quantities
    # identify the maximum quantity in the temporary quantity list
    for shoe_object in shoe_list:
        quanity_converted_integers = int(shoe_object.quantity)
        temp_quanity_list.append(quanity_converted_integers)
    
    if len(temp_quanity_list) >= 1:
        max_quanity = max(temp_quanity_list)

        # If the stock quantity matches the maximum quantity identified above,
        # create a temporary nested list that will store objects that have the maximum quanity identified, with the attribute details listed.
        # Format the items this relates to in a table using the tabulate module
        # Print out the the shoe(s) included in the table is for sale.
        max_shoe_list_attribute_detail_list = []
        for shoe_object in shoe_list:
            if shoe_object.quantity == str(max_quanity):
                shoe_details = shoe_object.__str__().split(",")

                if shoe_details not in max_shoe_list_attribute_detail_list:
                    max_shoe_list_attribute_detail_list.append(shoe_details)

        inventory_table = tabulate(max_shoe_list_attribute_detail_list, headers= ["Country", "Code", "Product", "Cost", "Quantity"])
        print(f"The following shoe is for sale: \n {inventory_table}")
    else:
        print("There is no shoe inventory and so there are no items for sale.")


#==========Main Menu=============

# Create a menu that executes each function above.

menu = ""

while True:
    
    menu = input('''Select one of the following Options below by entering the relevant number:
        1 - View all shoe inventory
        2 - Capture new shoe inventory
        3 - Restock shoe inventory
        4 - Search for shoe
        5 - View shoe inventory value
        6 - View sale items
        7 - Exit
        : ''')

    if menu == "1":
        # If user selects 1, print out all of the the shoe inventory in a table
        read_shoes_data()
        view_all()
    
    elif menu == "2":
        # if user selects 2,request user to enter the data required to create a shoe object
        # capture data and update the inventory list for the new shoe item

        # Read shoe data from inventory file
        read_shoes_data()

        # Request user to enter country
        country = input("Enter the country: ")

        # Request user to enter code
        # Print out error if the SKU format is not followed and request user to try again
        while True:
            try:
                code = input("Enter the shoe SKU code: ")
                if code[0:3].upper() == "SKU" and int(code[3:])>0:
                    break
                else:
                    print("Error: The SKU code entered is inavilid. Please enter a valid code beginning with the 'SKU'")
            except ValueError:
                print("Error: Invalid code. The code should consist of numbers after the 'SKU'")

        product = input("Enter the shoe product name: ")

        # Request user to enter cost
        # Print out error if the user tries to enter a value that's not a number or a negative number
        while True:
            try:
                cost = float(input("Enter the shoe cost per item: "))
                if cost >= 0:
                    break
                else:
                    print("Error: The number entered for cost cannot be less than 0. Please try again")
            except ValueError:
                print("Error: Invalid value. Please enter a float or integer number.")

         # Request user to enter quantity
        # Print out error if the user tries to enter a value that's not a number or a negative number
        while True:
            try:
                quantity = int(input("Enter the shoe quantity: "))
                if quantity >= 0:
                    break
                else:
                    print("Error: The number entered for quantity cannot be less than 0. Please try again")
            except ValueError:
                print("Error: Invalid value. Please enter a float or integer number.")
        
        # Call capture_shoes function to create a new object
        new_shoe_object = capture_shoes(country, code, product, cost, quantity)

        # Add the additional shoe captured to the shoe inventory file
        with open("inventory.txt", "a") as file:
            file.write(f"{new_shoe_object}\n")

        # Print out message to confirm that the process of capturing the new shoe item is compelete
        print("Done- New shoe stock captured.")

    # if user selects "e", exit them from the program and diplay to notify them of that
    
    elif menu == "3":
        # if user selects 3, enable user to restock for the shoe with the lowest quanity inventory on hand
        read_shoes_data()
        re_stock()

    elif menu == "4":
        # If user selects 4, call the read_shoes and search_shoe function to enable the user to search
        # for a shoe item based on the SKU code
        read_shoes_data()
        search_shoe()

    elif menu == "5":
        # If user selects 5, call the value_per_item() function to enable user to view the inventory value
        # of each shoe in a table.
        value_per_item()       

    elif menu == "6":
        # If user selects 6, call the highest_qty() function to show the user the shoe item(s) with the
        # highest quanity of inventory, which will be the sale item(s)
        # Print out table to display this
        read_shoes_data()
        highest_qty()        

    elif menu == '7':
        print('You are now exiting. Goodbye!')
        exit()

    else:
        print("Error: You have selected an invalid option. Please try again and enter one of the menu option numbers available.")