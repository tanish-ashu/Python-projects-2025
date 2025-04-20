import csv
from datetime import date, timedelta
from mysql.connector import Error

# We need the connection function from the other file
from db_connection import create_db_connection

def add_expense(conn, expense_date, category, amount, description):
    """ Adds a new expense record to the database. """
    cursor = conn.cursor()
    query = "INSERT INTO expenses (expense_date, category, amount, description) VALUES (%s, %s, %s, %s)"
    try:
        cursor.execute(query, (expense_date, category, amount, description))
        conn.commit() # Save the changes to the database
        print("Expense added successfully.")
    except Error as e:
        print(f"Error adding expense: '{e}'")
    finally:
        cursor.close()

def get_expenses_summary(conn, start_date, end_date):
    """ Gets a summary of expenses grouped by category within a date range. """
    cursor = conn.cursor(dictionary=True) # Get results as dictionaries
    query = """
        SELECT category, SUM(amount) as total_amount
        FROM expenses
        WHERE expense_date BETWEEN %s AND %s
        GROUP BY category
        ORDER BY total_amount DESC
    """
    summary = []
    try:
        cursor.execute(query, (start_date, end_date))
        summary = cursor.fetchall() # Fetch all matching rows
    except Error as e:
        print(f"Error fetching summary: '{e}'")
    finally:
        cursor.close()
    return summary

def get_all_expenses(conn):
    """ Fetches all expense records from the database. """
    cursor = conn.cursor(dictionary=True)
    query = "SELECT id, expense_date, category, amount, description FROM expenses ORDER BY expense_date DESC"
    expenses = []
    try:
        cursor.execute(query)
        expenses = cursor.fetchall()
    except Error as e:
        print(f"Error fetching all expenses: '{e}'")
    finally:
        cursor.close()
    return expenses

def export_expenses_to_csv(conn, filename="expenses_export.csv"):
    """ Exports all expenses to a CSV file. """
    expenses = get_all_expenses(conn)
    if not expenses:
        print("No expenses to export.")
        return

    try:
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            # Define the header row
            fieldnames = ['id', 'expense_date', 'category', 'amount', 'description']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader() # Write the header
            writer.writerows(expenses) # Write the expense data
        print(f"Expenses successfully exported to {filename}")
    except IOError as e:
        print(f"Error writing to CSV file: '{e}'")

# --- Helper functions for date ranges ---

def get_current_week_range():
    """ Returns the start and end date of the current week (Mon-Sun). """
    today = date.today()
    start_of_week = today - timedelta(days=today.weekday()) # Monday
    end_of_week = start_of_week + timedelta(days=6) # Sunday
    return start_of_week, end_of_week

def get_current_month_range():
    """ Returns the start and end date of the current month. """
    today = date.today()
    start_of_month = today.replace(day=1)
    # Find the last day of the month
    next_month = today.replace(day=28) + timedelta(days=4) # Go to next month
    end_of_month = next_month - timedelta(days=next_month.day) # Go back to last day of current month
    return start_of_month, end_of_month

