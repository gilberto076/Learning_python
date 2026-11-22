import json
import os
from decimal import Decimal
import uuid

from validators import id_exists

# This module handles the storage of expenses in a JSON file.
# It is responsible for reading the saved list of expenses and adding new ones.

def load_expenses(archivo="data/gastos.json"):
    # If the file does not exist, the application starts with an empty list.
    if not os.path.exists(archivo):
        return []

    # Open the JSON file and load its contents as a Python list of expenses.
    with open(archivo, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            # Return an empty list if the file is empty or contains invalid JSON.
            return []

def save_expenses(nuevo_gasto, archivo="data/gastos.json"):
    # Load the current expense list so we can append the new expense.
    gastos = load_expenses(archivo)

    # Add the new item at the end of the list.
    gastos.append(nuevo_gasto)

    # Save the complete list back to the JSON file.
    with open(archivo, "w") as f:
        json.dump(gastos, f, default=str, indent=2)


# generation: uses id_exists
def generate_unique_id(existing):
    new_id = str(uuid.uuid4())

    while id_exists(new_id, existing):
        new_id = str(uuid.uuid4())

    return new_id


    save_expenses(expense)

def search_expense_by_id(expense_id, expenses=None):
    if expenses is None:
        expenses = load_expenses()
    for expense in expenses:
        if expense.get("id") == expense_id:
            return expense
    return None

