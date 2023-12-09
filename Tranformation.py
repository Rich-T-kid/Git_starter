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

# Orchestrates the program's execution.
def main():
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

# Entry point of the program.
if __name__ == "__main__":
    main()
