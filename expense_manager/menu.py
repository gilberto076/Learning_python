

from decimal import Decimal, InvalidOperation
from email import message
import uuid
from storage import  load_expenses, save_data, generate_unique_id
from validators import (
    validate_id,
    validate_required,
    validate_amount,
    validate_date,
    validate_category,
)

categories = ["Food", "Transportation", "Housing", "Health", "Education", "Entertainment","Services", "Other"]

# showing the menu to the user 
def show_menu():
    ...
    print("...Expense manager choise an opcion...")
    print("...1.add new expensive...")
    print("...2.edit an expensive...")
    print("...3.delete an expense")
    print("...4.list expensive...")
    print("...press Enter to quit")

# validating data enter 
    options = [1,2,3,4]
    while True:

       enter  = input("Enter your choise (or press Enter to quit )")
       if enter  == "":
          print("Saliendo...")
          break
       
       try:
         choise = int(enter) 
        
       except ValueError:
         print("Opcion no valida. Intenta de nuevo.")
         continue 

       if choise in options:
          print (f"Has elegido {choise}")
          return  choise
       else:
         print("Opcion no valida. Intenta de nuevo.")



#printing the menu and getting the user choise
def get_user_choice():
    choise = show_menu()
    print(f"User choice: {choise}")

    


def run_menu():
    ...

def prompt_validated(message, validator, *args, ):
    while True:
        raw = input(message) 
        cleaned, error = validator(raw, *args)

        if error:
            print(error)
            continue

        return cleaned



def handle_add_expense():
     
    id =   validate_id (generate_unique_id( load_expenses()))

       

    description = prompt_validated(
        "Enter description: ",
        validate_required,
        "Description"
    )

    amount = prompt_validated(
        "Enter amount: ",
        validate_amount
    )

    show_categories()

    category = prompt_validated(
        "Enter category: ",
        validate_category,
        categories
    )

    date = prompt_validated(
        "Enter date (DD/MM/YYYY): ",
        validate_date
    )


    data = save_data(id ,description, amount, category, date)


    return data
 

        

def show_categories():
    categories1 = categories
    print("Available categories:")
    for category in categories1:
        print(category)


def handle_edit_expense():
    ...


def handle_delete_expense():
    ...


def handle_list_expensive():
    ...
