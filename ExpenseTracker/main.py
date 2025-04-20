from db_connection import create_db_connection
import expense_operations as exp_ops 
import budget_operations as bud_ops
import visualization as viz
import datetime
from datetime import timedelta


def get_date_input(prompt="Enter date (YYYY-MM-DD, leave blank for today): "):
    """ Gets a valid date input from the user. """
    while True:
        date_str = input(prompt).strip()
        if not date_str: # If blank, use today's date
            return datetime.date.today()
        try:
            return datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

def get_float_input(prompt="Enter amount: "):
    """ Gets a valid positive float input from the user. """
    while True:
        try:
            value = float(input(prompt).strip())
            if value >= 0:
                return value
            else:
                print("Amount cannot be negative.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_year_month_input():
    """ Gets valid year and month input from the user. """
    today = datetime.date.today()
    while True:
        try:
            year_str = input(f"Enter year (e.g., {today.year}): ").strip()
            year = int(year_str) if year_str else today.year # Default to current year

            month_str = input(f"Enter month (1-12, e.g., {today.month}): ").strip()
            month = int(month_str) if month_str else today.month # Default to current month

            if 1 <= month <= 12 and year > 1900: # Basic validation
                 return year, month
            else:
                 print("Invalid year or month.")
        except ValueError:
            print("Invalid input. Please enter numbers for year and month.")


def main_menu(conn):
    """ Displays the main menu and handles user choices. """
    while True:
        print("\n--- Expense Tracker Menu ---")
        print("1. Add New Expense")
        print("2. View Weekly Summary")
        print("3. View Monthly Summary")
        print("4. Set/Update Budget for Category/Month")
        print("5. Check Budget Status for Category/Month")
        print("6. Export All Expenses to CSV")
        print("7. Exit")
        print("---------------------------")

        choice = input("Enter your choice (1-7): ").strip()

        if choice == '1':
            # Add Expense
            print("\n-- Add Expense --")
            exp_date = get_date_input()
            category = input("Enter category (e.g., Food, Transport, Bills): ").strip()
            amount = get_float_input("Enter amount: ")
            description = input("Enter description (optional): ").strip()

            if not category: # Basic validation
                print("Category cannot be empty.")
                continue

            exp_ops.add_expense(conn, exp_date, category, amount, description)

            # Check budget immediately after adding
            year, month = exp_date.year, exp_date.month
            budget_status = bud_ops.check_overspending(conn, category, year, month)
            if budget_status is not None and budget_status['overspent']:
                 print(f"!!! ALERT: Adding this expense made you exceed the budget for {category} in {year}-{month:02d} !!!")
                 print(f"    Budget: {budget_status['budget']:.2f}, Now Spent: {budget_status['spent']:.2f}")


        elif choice == '2':
            # Weekly Summary
            print("\n-- Weekly Summary (Current Week) --")
            start_week, end_week = exp_ops.get_current_week_range()
            summary = exp_ops.get_expenses_summary(conn, start_week, end_week)
            viz.display_summary(summary, f"Weekly Summary ({start_week} to {end_week})")

        elif choice == '3':
            # Monthly Summary
            print("\n-- Monthly Summary (Current Month) --")
            start_month, end_month = exp_ops.get_current_month_range()
            summary = exp_ops.get_expenses_summary(conn, start_month, end_month)
            viz.display_summary(summary, f"Monthly Summary ({start_month.strftime('%B %Y')})")

        elif choice == '4':
            # Set Budget
            print("\n-- Set/Update Budget --")
            category = input("Enter category to set budget for: ").strip()
            year, month = get_year_month_input()
            amount = get_float_input(f"Enter budget amount for {category} in {year}-{month:02d}: ")

            if not category:
                print("Category cannot be empty.")
                continue

            bud_ops.set_budget(conn, category, year, month, amount)

        elif choice == '5':
            # Check Budget Status
            print("\n-- Check Budget Status --")
            category = input("Enter category to check budget for: ").strip()
            year, month = get_year_month_input()

            if not category:
                print("Category cannot be empty.")
                continue

            status = bud_ops.check_overspending(conn, category, year, month)
            if status is None:
                 print(f"No budget has been set for '{category}' in {year}-{month:02d}.")
            else:
                 viz.display_budget_status(status) # Display the detailed status

        elif choice == '6':
            # Export to CSV
            print("\n-- Export Expenses --")
            filename = input("Enter filename (leave blank for 'expenses_export.csv'): ").strip()
            if not filename:
                filename = "expenses_export.csv"
            elif not filename.lower().endswith('.csv'):
                 filename += ".csv" # Add extension if missing

            exp_ops.export_expenses_to_csv(conn, filename)

        elif choice == '7':
            # Exit
            print("Exiting Expense Tracker. Goodbye!")
            break # Exit the while loop

        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    print("Starting Expense Tracker...")
    # Establish database connection once
    db_conn = create_db_connection()

    # Only proceed if the connection is successful
    if db_conn and db_conn.is_connected():
        # Run the main application menu
        main_menu(db_conn)
        # Close the connection when the application exits
        db_conn.close()
        print("Database connection closed.")
    else:
        print("Application cannot start without a database connection.")

