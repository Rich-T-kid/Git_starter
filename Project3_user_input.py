# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 16:29:22 2023

@author: seamu
"""

def write_to_file(data, filename="loan_application_data.txt"):
    try:
        with open(filename, "a") as file:
            file.write(data + "\n")
        print("Data successfully written to", filename)
    except Exception as e:
        print(f"Error writing to {filename}: {e}")

def calculate_net_profit_margin(net_income, net_sales):
    return net_income / net_sales

def calculate_liquidity_ratio(current_assets, current_liabilities):
    return current_assets / current_liabilities

def get_user_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid numerical value.")

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
            
def assign_net_profit_margin_rating(net_profit_margin):
    if net_profit_margin >= 0.2:
        return "Excellent"
    elif net_profit_margin >= 0.1:
        return "Good"
    else:
        return "Poor"

def assign_liquidity_ratio_rating(liquidity_ratio):
    if liquidity_ratio >= 1.5:
        return "Excellent"
    elif liquidity_ratio >= 1:
        return "Good"
    else:
        return "Poor"

def assign_business_credit_rating(business_credit):
    if business_credit >= 80:
        return "Excellent"
    elif business_credit >= 60:
        return "Good"
    else:
        return "Poor"

def assign_personal_credit_rating(personal_credit):
    if personal_credit >= 720:
        return "Excellent"
    elif personal_credit >= 680:
        return "Good"
    else:
        return "Poor"

def evaluate_loan_eligibility(net_profit_margin_rating, liquidity_ratio_rating, business_credit_rating, personal_credit_rating):
    # Check if all ratings meet the minimum criteria or any rating is "Excellent"
    eligibility_conditions = [
        rating in ["Excellent", "Good"]
        for rating in [net_profit_margin_rating, liquidity_ratio_rating, business_credit_rating, personal_credit_rating]
    ]

    # If all conditions are True, the applicant is likely eligible for a loan
    if all(eligibility_conditions):
        return "Congratulations! You are likely eligible for a loan."
    else:
        return "Sorry, your current financial metrics do not meet the minimum criteria for a loan."


def main():
    # Get inputs from the user
    net_income = get_user_input("Enter Net Income: $")
    net_sales = get_user_input("Enter Net Sales: $")
    current_assets = get_user_input("Enter Current Assets: $")
    current_liabilities = get_user_input("Enter Current Liabilities: $")

   # Calculate ratios
    net_profit_margin = calculate_net_profit_margin(net_income, net_sales)
    liquidity_ratio = calculate_liquidity_ratio(current_assets, current_liabilities)
    business_credit = get_business_credit()
    personal_credit = get_personal_credit()

    # Assign ratings
    net_profit_margin_rating = assign_net_profit_margin_rating(net_profit_margin)
    liquidity_ratio_rating = assign_liquidity_ratio_rating(liquidity_ratio)
    business_credit_rating = assign_business_credit_rating(business_credit)
    personal_credit_rating = assign_personal_credit_rating(personal_credit)

    # Display results
    print("\nResults with Ratings:")
    print(f"Net Profit Margin Ratio: {net_profit_margin:.2%} - Rating: {net_profit_margin_rating}")
    print(f"Liquidity Ratio: {liquidity_ratio:.2} - Rating: {liquidity_ratio_rating}")
    print(f"Business Credit Score: {business_credit} - Rating: {business_credit_rating}")
    print(f"Personal Credit Score: {personal_credit} - Rating: {personal_credit_rating}")

    # Evaluate loan eligibility
    loan_eligibility_result = evaluate_loan_eligibility(net_profit_margin_rating, liquidity_ratio_rating, business_credit_rating, personal_credit_rating)
    print("\nLoan Eligibility:", loan_eligibility_result)

    # Collect data as a string
    data_to_write = f"Net Profit Margin Ratio: {net_profit_margin:.2%}, " \
                    f"Liquidity Ratio: {liquidity_ratio:.2}, " \
                    f"Business Credit Score: {business_credit}, " \
                    f"Personal Credit Score: {personal_credit}, " \
                    f"Loan Eligibility: {loan_eligibility_result}"

    # Write data to a file
    write_to_file(data_to_write)

if __name__ == "__main__":
    main()
