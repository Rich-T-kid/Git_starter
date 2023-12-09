# main file where app will actually run. 
# Calculates and returns the net profit margin ratio.
def calculate_net_profit_margin(net_income, net_sales):
    return net_income / net_sales

# Calculates and returns the liquidity ratio.
def calculate_liquidity_ratio(current_assets, current_liabilities):
    return current_assets / current_liabilities

# Takes user input, ensuring it's a valid numerical value.
def get_user_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid numerical value.")

# Gets the business credit score from the user within a specified range.
def get_business_credit():
    while True:
        try:
            business_credit = int(input("Enter your business credit score (1-100): "))
            if 1 <= business_credit <= 100:
                return business_credit
            else:
                print("Business credit score must be between 1 and 100.")
        except ValueError:
            print("Please enter a valid numerical value.")

# Gets the personal credit score from the user within a specified range.
def get_personal_credit():
    while True:
        try:
            personal_credit = int(input("Enter your personal credit score (300-850): "))
            if 300 <= personal_credit <= 850:
                return personal_credit
            else:
                print("Personal credit score must be between 300 and 850.")
        except ValueError:
            print("Please enter a valid numerical value.")

# Assigns a rating based on the net profit margin ratio.
def assign_net_profit_margin_rating(net_profit_margin):
    if net_profit_margin >= 0.2:
        return .8  # Good
    elif net_profit_margin >= 0.1:
        return 1  # Neutral
    else:
        return 1.2  # Bad

# Assigns a rating based on the liquidity ratio.
def assign_liquidity_ratio_rating(liquidity_ratio):
    if liquidity_ratio >= 1.5:
        return .8  # Good
    elif liquidity_ratio >= 1:
        return 1  # Neutral
    else:
        return 1.2  # Bad
# Assigns a rating based on the liquidity ratio.
def assign_liquidity_ratio_rating(liquidity_ratio):
    return liquidity_ratio
    
# Assigns a rating based on the business credit score.
def assign_business_credit_rating(business_credit):
    if business_credit >= 80:
        return .8  # Good
    elif business_credit >= 60:
        return 1  # Neutral
    else:
        return 1.4  # Bad

# Assigns a rating based on the personal credit score.
def assign_personal_credit_rating(personal_credit):
    if personal_credit >= 720:
        return .9  # Good
    elif personal_credit >= 680:
        return 1.1  # Neutral
    else:
        return 1.3  # Bad

# Evaluates loan eligibility by multiplying individual ratings.
def evaluate_loan_eligibility(net_profit_margin_rating, liquidity_ratio_rating, business_credit_rating, personal_credit_rating):
    # Multiply all ratings to get a risk factor
    risk_factor = net_profit_margin_rating * liquidity_ratio_rating * business_credit_rating * personal_credit_rating
    return round(risk_factor, 3)
  
def main():
  pass
import json
from datetime import datetime, timedelta
 # Get financial inputs from the user.
    net_income = get_user_input("Enter Net Income: $")
    net_sales = get_user_input("Enter Net Sales: $")
    current_assets = get_user_input("Enter Current Assets: $")
    current_liabilities = get_user_input("Enter Current Liabilities: $")

    # Calculate financial ratios.
    net_profit_margin = calculate_net_profit_margin(net_income, net_sales)
    liquidity_ratio = calculate_liquidity_ratio(current_assets, current_liabilities)

    # Get credit scores from the user.
    business_credit = get_business_credit()
    personal_credit = get_personal_credit()

    # Assign ratings based on financial ratios and credit scores.
    net_profit_margin_rating = assign_net_profit_margin_rating(net_profit_margin)
    liquidity_ratio_rating = assign_liquidity_ratio_rating(liquidity_ratio)
    business_credit_rating = assign_business_credit_rating(business_credit)
    personal_credit_rating = assign_personal_credit_rating(personal_credit)

    # Display results with ratings.
    print("\nResults with Ratings:")
    print(f"Net Profit Margin Ratio: {net_profit_margin:.2%} - Rating: {net_profit_margin_rating}")
    print(f"Liquidity Ratio: {liquidity_ratio:.2} - Rating: {liquidity_ratio_rating}")
    print(f"Business Credit Score: {business_credit} - Rating: {business_credit_rating}")
    print(f"Personal Credit Score: {personal_credit} - Rating: {personal_credit_rating}")

    # Evaluate loan eligibility and display the risk factor.
    risk_factor = evaluate_loan_eligibility(net_profit_margin_rating, liquidity_ratio_rating, business_credit_rating, personal_credit_rating)
    print("\nRisk Factor:", risk_factor)

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
    change = abs(current_value - previous_value)
    if change >= threshold:
        print(f"There is a significant change of {change} from {previous_value} to {current_value}.")
    return change >= threshold

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
