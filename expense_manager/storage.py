import json

def save_expenses(archivo="data/gastos.json", gastos=[]):
    with open(archivo, "w") as f:
        json.dump(gastos, f, default=str)   # Decimal -> string
