

from decimal import Decimal, InvalidOperation
import uuid

gastos = []

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
        

        while True:
          description = input("Enter the description of the expense: ").strip()
          amount_input = input("Enter the amount of the expense: ").strip()
          category = input("Enter the category of the expense: ").strip()
          date = input("Enter the date of the expense DD/MM/AAAA: ").strip()

          # --- Validation ---
          if not description:
           print("Description cannot be empty.")
           continue

          if not category:
           print("Category cannot be empty.")
           continue

          if not date:
           print("Date cannot be empty.")
           continue

          try:
           amount = Decimal(amount_input)
           if amount <= 0:
             print("Amount must be greater than zero.")
             continue
          except (InvalidOperation, TypeError):
            print("Amount must be a valid number.")
            continue

          break  # all good, exit the loop


        new_expense = {
            "id": str(uuid.uuid4()),
            "description": description,
            "amount": Decimal(str(amount)),   # convert to Decimal
            "category": category,
            "date": date,
        }
        gastos.append(new_expense)
        return gastos

        




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
