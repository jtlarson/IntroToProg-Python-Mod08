# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# <Your Name>,<Today's Date>,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #
import pickle # used for saving list
import os # used by read_data_from_file function

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = [] # list of product objects created via Person class
name_and_price_lst = [] # single product and price list

class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the product's  name
        product_price: (float) with the product's standard price (no $)
    methods:
        __str__: (string) in format "<product_name>,<product_price>"
        to_string: (string) alias of __str__
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        jtlarson,2022-08-29,Adding constructor and properties to class
    """
    # TODO: Add Code to the Product class
    # -- Constructor --
    def __init__(self, product_name, product_price):
        # 	   -- Attributes --
        self.product_name = product_name
        self.product_price = product_price

    # -- Properties --
    # product_name
    @property
    def product_name(self): # (getter or accessor)
        return str(self.__product_name_str)

    @product_name.setter  # The NAME MUST MATCH the property's!
    def product_name(self, value):  # (setter or mutator)
        if str(value).isascii() == True:
            self.__product_name_str = value
        else:
            raise Exception("Is that the best name you can come up with? (should be ascii)")

    # product_price
    @property
    def product_price(self): # (getter or accessor)
        return float(self.__product_price_flt)

    @product_price.setter  # The NAME MUST MATCH the property's!
    def product_price(self, value):  # (setter or mutator)
        try:
            self.__product_price_flt = float(value)
        except:
            raise Exception("Numbers and decimal only. Example: 4.99")

    # -- Methods --
    def to_string(self):
        return self.__str__()

    def __str__(self):
        return str(self.product_name) + ',' + str(self.product_price)

# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        jtlarson,2022-08-29,Modified code to complete assignment 8
    """
    # TODO: Add Code to process data from a file
    @staticmethod
    def read_data_from_file(binary_file_name):  # pickle.load file using try, except with custom errors
        """ Reads data from a file into a list. Uses custom exception handling
        in multiple 'exception' blocks to trigger friendly user output.

        :param file_name: (string) with name of file
        :return: (list) of product objects
        """
        list_of_product_obj = []
        list_of_product_obj.clear()  # clear current data
        try:  # Using 'try, except' to provide enhanced suggestions if loading any rows from file fails
            file = open(binary_file_name, "rb")  # if it's there, read it
        except FileNotFoundError as e:
            IO.output_message(message="file_not_found")
            try:  # Using 'try, except' to provide enhanced suggestions if loading any rows from file fails
                file = open(binary_file_name, "ab+")  # Create it and read the contents
            except Exception as e:
                print(e)
                print(type(e))
                print(e.__doc__)
                print(e.__str__())
                IO.output_message(message="file_write_error", data=os.getcwd())
                exit()
        try:
            list_of_product_obj = pickle.load(file)
            file.close()
        except EOFError as e:  # This error is expected if the file doesn't have a list yet--just move on.
            file.close()
        except Exception as e:
            IO.output_message(message="unpickle_error")
            file.close()
        return list_of_product_obj
    # TODO: Add Code to process data to a file
    @staticmethod
    def save_data_to_file(file_name, product_list):
        """ pickle topping list for later

        :param file_name: (string) with name of file
        :param product_list: (list) of objects to write to file
        :return: (list) of saved product objects
        """
        # Open the file and pickle the 'sandwich' list
        file = open(file_name, "wb")
        pickle.dump(product_list,file)
        file.close()
        return product_list
# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    # TODO: Add docstring
    """Handles input and output to user

    methods:
        output_menu_tasks: Display formatted string of menu options
        input_menu_choice: Returns string input by user
        show_current_product: Formats list for display to user
        input_product: Creates list containing product, price collected from user input
        output_message: Dictionary of user message to display with (optional) additional data

    changelog: (When,Who,What)
        jtlarson,2022-08-22,Created class for Assignment 07
        jtlarson,2022-08-30,Modifying methods to current script
    """
    # TODO: Add code to show menu to user
    @staticmethod
    def output_menu_tasks(): #function to display main menu
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) View list of products
        2) Add a product to list
        3) Save data to file and exit
        4) Exit without saving
        ''')
        #print()  # Add an extra line for looks

    # TODO: Add code to get user's choice
    @staticmethod
    def input_menu_choice(): #function: ask user for selection and return
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
        #print()  # Add an extra line for looks
        return choice

    # TODO: Add code to show the current data from the file to user
    @staticmethod
    def show_current_product(product_list):
        """ Shows the current list of products loaded/entered

        :param product_list: (list) of products
        :return: nothing
        """
        if lstOfProductObjects:  # if there are any toppings
            max_product_chars = 0  # the length of the prod
            # Find the longest task name
            for item in lstOfProductObjects:
                if len(item.product_name) > max_product_chars:
                    max_product_chars = len(item.product_name)
            # Display product list between === sized to fit
            print(" " * 7, "Product", " " * (max_product_chars - 7), "|", "Price")
            print(" " * 7, "-" * (max_product_chars + 9))
            for item in lstOfProductObjects:
                print(" " * 7, item.product_name, \
                      " " * (max_product_chars - len(item.product_name)), "|", item.product_price)
            print()

    # TODO: Add code to get product data from user
    #function: ask user for product (string) to add (try, except?)
    @staticmethod
    def input_product():
        """ Ask the user for a product name and price

        :return: (list) of product name, price
        """
        product = []
        while True:
            name = str(input("Type in a product name: ")).strip()

            if name.isascii():
                product.append(name)
                break
            else:
                print("Invalid name. What else can I add?")
        while True:
            try:
                value = float(input("Type in a product value (no $ sign): "))
                if float(value) > 0:
                    print("Thank you")
                    product.append(value)
                    break
                else:
                    print("Needs to be a positive number")
                    continue
            except Exception as e:
                print("Invalid price. Enter numbers and decimal only")
        return product

    @staticmethod
    def output_message(message, data = ''): #function to display comments: greeting, eating, take it to go, dash
        """  Messages for user
        :param message: (string) keyword of message to display
        :param data: (string) Optional additional data to display
        :return: Nothing
        """
        message_dict = {'file_not_found': "Expected file not found",
                        'fresh_sandwich': "You look like you could use a fresh sandwich! (no list in file)",
                        'file_write_error': "Unknown error accessing/creating save file--verify write access to:",
                        'empty_file': "There's no data to save to file",
                        'unpickle_error': "The save file appears to be damaged (can't unpickle file)",
                        'save_confirmation': "Saving products to file.",
                        'exit_now': "Exiting the program.",
                        'unknown': "I didn't understand that. Try again"
                        }
        print(message_dict[message], data)
# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #
# TODO: Add Data Code to the Main body

# Load data from file into a list of product objects when script starts
lstOfProductObjects = FileProcessor.read_data_from_file(strFileName) #Open file and load contents if found

while True:
    #show the menu, and ask for user's choice
    IO.output_menu_tasks()
    menu_choice = IO.input_menu_choice() # Get user's menu option choice

    # Show user current data in the list of product objects
    if menu_choice == '1':  # View list of products
        IO.show_current_product(lstOfProductObjects)
        continue  # to show the menu

    # Let user add data to the list of product objects
    elif menu_choice == '2':  # Add a product to list (append)
        name_and_price_lst = IO.input_product()
        lstOfProductObjects.append(Product(name_and_price_lst[0], name_and_price_lst[1]))
        continue  # to show the menu

    # let user save current data to file and exit program
    elif menu_choice == '3':  # Save data to file and exit (try: pickle current list)
        if len(lstOfProductObjects) == 0:
            IO.output_message('empty_file')
            continue
        else:
            IO.output_message('save_confirmation')
            lstOfProductObjects = FileProcessor.save_data_to_file(strFileName, lstOfProductObjects)
            break  # exit the program

    elif menu_choice == '4':  # Exit without saving
            break  # exit the program

    else:
        IO.output_message("unknown")
        continue
#exit
# Main Body of Script  ---------------------------------------------------- #