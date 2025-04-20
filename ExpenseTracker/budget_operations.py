from mysql.connector import Error
from datetime import date, timedelta



def set_budget(conn, category, year, month, amount):
    """ Sets or updates the budget for a specific category and month/year. """
    cursor = conn.cursor()
    query = """
        INSERT INTO budgets (category, budget_year, budget_month, amount)
        VALUES (%s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE amount = VALUES(amount)
    """
    try:
        cursor.execute(query, (category, year, month, amount))
        conn.commit()
        print(f"Budget for {category} in {year}-{month:02d} set/updated to {amount:.2f}.")
    except Error as e:
        print(f"Error setting budget: '{e}'")
    finally:
        cursor.close()




def get_budget(conn, category, year, month):
    """ Retrieves the budget amount for a specific category and month/year. """
    cursor = conn.cursor()
    query = """
        SELECT amount FROM budgets
        WHERE category = %s AND budget_year = %s AND budget_month = %s
    """
    budget_amount = None
    try:
        cursor.execute(query, (category, year, month))
        result = cursor.fetchone()
        if result:
            budget_amount = result[0] # getting first column result
    except Error as e:
        print(f"Error getting budget: '{e}'")
    finally:
        cursor.close()
    return budget_amount



    

def get_spending_for_category_month(conn, category, year, month):
    """ Calculates the total spending for a category in a specific month/year. """
    cursor = conn.cursor()
    # Calculate the start and end date for the given month/year
    start_date = date(year, month, 1)
    # Find the last day of the month
    next_month = start_date.replace(day=28) + timedelta(days=4)
    end_date = next_month - timedelta(days=next_month.day)

    query = """
        SELECT SUM(amount) FROM expenses
        WHERE category = %s AND expense_date BETWEEN %s AND %s
    """
    total_spent = 0.0
    try:
        cursor.execute(query, (category, start_date, end_date))
        result = cursor.fetchone()
        if result and result[0] is not None: # Check if SUM returned a value
            total_spent = float(result[0])
    except Error as e:
        print(f"Error calculating spending: '{e}'")
    finally:
        cursor.close()
    return total_spent





def check_overspending(conn, category, year, month):
    """ Checks if spending exceeds the budget for a category/month and returns details. """
    budget = get_budget(conn, category, year, month)
    if budget is None:
        # No budget set for this category/month
        return None # Indicate no budget was found

    spent = get_spending_for_category_month(conn, category, year, month)
    overspent_amount = spent - budget

    return {
        "category": category,
        "year": year,
        "month": month,
        "budget": budget,
        "spent": spent,
        "overspent": overspent_amount > 0,
        "overspent_amount": max(0, overspent_amount) # Show 0 if not overspent
    }

