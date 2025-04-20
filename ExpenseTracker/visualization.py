# visualization.py
# Handles display of summaries using Matplotlib and text alerts.

# Import the plotting library
import matplotlib.pyplot as plt

def display_summary(summary_data, title="Spending Summary"):
    """
    Displays the expense summary in a simple text format
    and generates a bar chart using Matplotlib.
    """
    print(f"\n--- {title} ---")
    if not summary_data:
        print("No spending data found for this period.")
        return

    # --- Text Summary (keeping this for clarity) ---
    total_spending = sum(item['total_amount'] for item in summary_data)
    print(f"Total Spending: {total_spending:.2f}")
    print("-" * (len(title) + 6))
    print("Spending by Category:")
    for item in summary_data:
        category = item['category']
        amount = item['total_amount']
        print(f"{category:<15}: {amount:>8.2f}")
    print("-" * (len(title) + 6))
    # --- End Text Summary ---


    # --- Matplotlib Bar Chart ---
    try:
        # Prepare data for plotting
        categories = [item['category'] for item in summary_data]
        amounts = [float(item['total_amount']) for item in summary_data] # Ensure amounts are float

        # Create the bar chart
        plt.figure(figsize=(10, 6)) # Set figure size (width, height in inches)
        plt.bar(categories, amounts, color='skyblue') # Create bars

        # Add labels and title
        plt.xlabel("Category")
        plt.ylabel("Amount Spent")
        plt.title(title)
        plt.xticks(rotation=45, ha='right') # Rotate category labels if they overlap
        plt.tight_layout() # Adjust layout to prevent labels overlapping

        # Display the plot in a new window
        print("\nDisplaying spending summary chart...")
        plt.show()

    except Exception as e:
        print(f"\nCould not generate plot. Error: {e}")
        print("Please ensure Matplotlib is installed correctly ('pip install matplotlib').")
    # --- End Matplotlib Bar Chart ---


def display_budget_status(status):
    """
    Displays the budget status and alerts for overspending (Text-based).
    No plotting needed here as text alerts are clearer for this purpose.
    """
    if status is None:
        # This means no budget was set for the checked category/month
        # print("No budget set for this category/period.") # Optional
        return False # Indicate no overspending (as no budget exists)

    print(f"\n--- Budget Status for {status['category']} ({status['year']}-{status['month']:02d}) ---")
    print(f"Budget Set : {status['budget']:.2f}")
    print(f"Total Spent: {status['spent']:.2f}")
    if status['overspent']:
        # Use a clear text alert for overspending
        print(f"!!! ALERT: Overspent by {status['overspent_amount']:.2f} !!!")
        return True # Indicate overspending occurred
    else:
        remaining = status['budget'] - status['spent']
        print(f"Remaining  : {remaining:.2f}")
        return False # Indicate not overspent

