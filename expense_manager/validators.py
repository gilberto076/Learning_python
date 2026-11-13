from decimal import Decimal, InvalidOperation
from datetime import datetime

# validating can not be empty  
def validate_required(value, field_name):

    value = value.strip()

    if not value:
        return None, f"{field_name} cannot be empty."

    return value, None

# validating amount 

MAX_AMOUNT = Decimal("99999.99")

def validate_amount(value):

    try:
        amount = Decimal(value.strip())
    except (InvalidOperation, TypeError):
        return None, "Amount must be a valid number."
    if not amount.is_finite():
        return None, "Amount must be a finite number."
    if amount <= 0:
        return None, "Amount must be greater than zero."
    if amount > MAX_AMOUNT:
        return None, f"Amount cannot exceed {MAX_AMOUNT}."
    return amount, None

# validating date format and if it is a valid date
def validate_date(value):

    try:
        date = datetime.strptime(
            value.strip(),
            "%d/%m/%Y"
        ).date()

        return date, None

    except (ValueError, AttributeError):
        return None, "Invalid date. Use DD/MM/YYYY."


#validating category and if it is in the available categories
def validate_category(value, available_categories):

    value, error = validate_required(
        value,
        "Category"
    )

    if error:
        return None, error

    if value not in available_categories:
        return None, "Category does not exist."

    return value, None

def validate_id(value):
    value, error = validate_required(value, "ID")
    if error:
        return None, error
    return value


# uniqueness: needs the collection
def id_exists(expense_id, expenses):
    for expense in expenses:
        if expense.get("id") == expense_id:
            return True
    return False


