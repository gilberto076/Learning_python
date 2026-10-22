

from decimal import Decimal, InvalidOperation

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



# Handling the "Add Expense" option
def handle_add_expense():
   ...
    



def show_categories():
    categories = ["Food", "Transportation", "Housing", "Health", "Education", "Entertaiment","Services", "Other"]
    print("Available categories:")
    for category in categories:
        print(category)

def handle_edit_expense():
    ...


def handle_delete_expense():
    ...


def handle_list_expensive():
    ...

