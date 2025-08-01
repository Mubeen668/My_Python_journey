# simple compound interest calculator
def compound_interest(principal, rate, time):

    amount = principal * (1 + rate / 100) ** time
    return amount - principal


try:
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the annual interest rate (in %): "))
    time = float(input("Enter the time (in years): "))

    if principal < 0 or rate < 0 or time < 0:
        print("Principal, rate, and time must be non-negative.")
        exit()

    interest = compound_interest(principal, rate, time)
    total_amount = principal + interest

    print(f"Compound Interest: {interest:.2f}")
    print(f"Total Amount after {time} years: {total_amount:.2f}")

except ValueError:
    print("Invalid input. Please enter numeric values.")
