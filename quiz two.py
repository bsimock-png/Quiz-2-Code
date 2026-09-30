
def calculate_monthly_payment(principal, annual_interest_rate, years):
        monthly_rate = annual_interest_rate / 100 / 12
        total_payments = years * 12
        if monthly_rate == 0:
            return principal / total_payments
        else:
            return principal * monthly_rate * (1 + monthly_rate) ** total_payments / ((1 + monthly_rate) ** total_payments - 1)

        principal = float(input("Enter the loan principal amount ($): ")) 
        annual_interest_rate = float(input("Enter the annual interest rate (%): "))
        years = int(input("Enter the loan term in (years): "))    

        monthly_payment = calculate_monthly_payment(principal, annual_interest_rate, years)
        print(f"\nYour estimated monthly payment is: ${monthly_payment:,.2f}")
