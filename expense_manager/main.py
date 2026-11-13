#import menu
#from validators import validate_id
#from storage import load_expenses, generate_unique_id
from  menu import handle_add_expense
def main():

   
   expense = handle_add_expense()
   print(f"Expense added: {expense }")


if __name__ == "__main__":
    main()
    
