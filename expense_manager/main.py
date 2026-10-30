import menu
import storage

def main():

   gastos =  menu.handle_add_expense()
   storage.save_expenses(gastos=gastos)
    


if __name__ == "__main__":
 main()
    
