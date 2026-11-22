
# expense_service.py
import uuid
from storage import load_expenses, save_expenses
from storage import load_expenses



def prompt_validated(message, validator, *args, ):
    while True:
        raw = input(message) 
        cleaned, error = validator(raw, *args)

        if error:
            print(error)
            continue

        return cleaned

#Create and save an expense / Crear y guardar un gasto
def add_expense(description, amount, category, date):
    expenses = load_expenses()

    expense = {
        "id": str(uuid.uuid4()),
        "description": description,
        "amount": amount,
        "category": category,
        "date": date,
    }
    save_expenses(expense)

    return expense
