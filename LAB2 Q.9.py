'''You are designing a software for a bank. The bank calculates interest on their RD accounts at
7.1% p.a. You need to develop the functionality, where the user can check their returns for a
given duration and for a given monthly installment amount. Note that the bank does not allow
monthly installment less than Rs. 500/- and the duration of RD should be atleast 6 months.
Check for valid and invalid inputs.'''


def calculate_rd_returns(installment_amount, duration_months, interest_rate=7.1):
    # Constants
    MIN_INSTALLMENT_AMOUNT = 500  # Minimum monthly installment amount
    MIN_DURATION_MONTHS = 6  # Minimum duration in months
    ANNUAL_INTEREST_RATE = interest_rate / 100  # Convert annual interest rate to decimal

    # Validate inputs
    if installment_amount < MIN_INSTALLMENT_AMOUNT:
        return "Invalid: Monthly installment amount should be at least Rs. 500"

    if duration_months < MIN_DURATION_MONTHS:
        return "Invalid: Duration of RD should be at least 6 months"

    # Calculate RD maturity amount
    total_amount = 0
    for month in range(1, duration_months + 1):
        monthly_interest = (total_amount + installment_amount) * (ANNUAL_INTEREST_RATE / 12)
        total_amount += installment_amount + monthly_interest

    return total_amount


# Input from the user
installment_amount = float(input("Enter the monthly installment amount (Rs.): "))
duration_months = int(input("Enter the duration of RD (in months): "))

# Calculate and display returns
result = calculate_rd_returns(installment_amount, duration_months)
print("Total amount in your RD account after {} months: Rs. {:.2f}".format(duration_months, result))
