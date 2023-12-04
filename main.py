# main file where app will actually run. 

def main():
  pass
import json
from datetime import datetime, timedelta

class Loan:
    def __init__(self, amount, duration, risk_factor) -> None:
        # Initialize the Loan object with amount, duration, and risk_factor attributes
        self.amount = amount
        self.duration = duration
        self.risk_factor = risk_factor

    def calculate_interest_rate(self):
        # Calculate the interest rate based on a base rate, risk premium, and risk factor
        base_rate = 0.05  
        risk_premium = self.risk_factor * 0.02  
        interest_rate = base_rate + risk_premium
        return interest_rate

class LoanManager:
    def __init__(self) -> None:
        # Initialize LoanManager with an empty list to store loans
        self.loans = []

    def collect_loan_data(self):
        # Collect user input for loan amount, duration, and risk factor
        amount = float(input("Enter loan amount: "))
        duration = int(input("Enter loan duration (in months): "))
        risk_factor = float(input("Enter risk factor: "))
        
        # Create a Loan object and append it to the list of loans with a timestamp
        loan = Loan(amount, duration, risk_factor)
        self.loans.append({"loan": loan.__dict__, "timestamp": timestamp()})

    def calculate_total_interest(self):
        # Calculate the total interest for all loans in the collection
        total_interest = 0
        for loan_data in self.loans:
            loan = Loan(**loan_data["loan"])
            interest_rate = loan.calculate_interest_rate()
            interest = loan.amount * interest_rate * loan.duration
            total_interest += interest
        return total_interest

    def analyze_since_first_day(self):
        # Check if there's a significant change in interest since the first day
        if len(self.loans) > 1:
            first_day_interest = self.calculate_total_interest()
            current_interest = self.loans[-1]["loan"]["amount"] * \
                               Loan(**self.loans[-1]["loan"]).calculate_interest_rate() * \
                               self.loans[-1]["loan"]["duration"]

            # If there's a significant change, return a message, otherwise, indicate no significant change
            if is_significant_change(current_interest, first_day_interest):
                return f"Significant change since the first day. Current interest: ${current_interest:.2f}, First day interest: ${first_day_interest:.2f}"
        return "No significant change since the first day."

    def write_to_file(self):
        # Write the list of loans to a JSON file
        filename = "loan_data.json"
        with open(filename, "w") as file:
            json.dump(self.loans, file)

def is_significant_change(current_value, previous_value, threshold=10):
    # Check if the difference between current and previous values is greater than or equal to the threshold
    return abs(current_value - previous_value) >= threshold

# Function to get timestamp
def timestamp():
    # Get the current timestamp in a formatted string
    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime("%B %d, %Y %H:%M:%S")
    return formatted_datetime

loan_manager = LoanManager()

while True:
    try:
        # Collect loan data, analyze changes, and print a message
        loan_manager.collect_loan_data()
        significant_change_message = loan_manager.analyze_since_first_day()
        print(significant_change_message)

        # Write loan data to a file
        loan_manager.write_to_file()

        # Prompt the user to continue or exit
        choice = input("Enter 'exit' to end, or press Enter to continue: ")
        if choice.lower() == "exit":
            break

    except ValueError:
        print("Invalid input. Please enter valid numeric values.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
  main()
