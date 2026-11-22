

from expense_service import add_expense, prompt_validated
from validators import (
    validate_required,
    validate_amount,
    validate_date,
    validate_category,
    validate_menu_enter
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
    choise = validate_menu_enter(options)
    return choise
   


#printing the menu and getting the user choise
def get_user_choice():
    choise = show_menu()
    print(f"User choice: {choise}")
    return choise
    



def handle_add_expense():
     
   # menu.py
    description = prompt_validated(
                  "Enter description: ",
                   validate_required,
                     "Description")

    amount      = prompt_validated(
                 "Enter amount: ",
                  validate_amount)
    
    show_categories()

    category    = prompt_validated(
                  "Enter category: ",
                   validate_category, 
                   categories)

    date        = prompt_validated(
                  "Enter date (DD/MM/YYYY): ",
                   validate_date)

    expense = add_expense(description, amount, category, date)
    
    print(f"Saved. New id: {expense['id']}")

    


def show_categories():
    categories1 = categories
    print("Available categories:")
    for category in categories1:
        print(category)


def handle_edit_expense():
    ...









def handle_delete_expense():
    print("Deleting an expense...")


def handle_list_expensive():
    print("Listing expenses...")

def run_menu():
    while True:
        choice = get_user_choice()

        if choice == 1:
            handle_add_expense()
        elif choice == 2:
            handle_edit_expense()
        elif choice == 3:
            handle_delete_expense()
        elif choice == 4:
            handle_list_expensive()
        else:
            print("Exiting...")
            break
    
    