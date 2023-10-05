#!usr/bin/env python3

def calculate_future_value(per_month, interest, years):
    monthly_interest_rate = interest / 12 / 100
    months = years * 12
    future_value = 0.0
    for i in range(1, months):
        future_value += per_month
        per_month = future_value * monthly_interest_rate
        future_value += per_month
    return future_value

def main():
    per_month = float(input('Enter monthly investment: $'))
    interest = float(input('Enter interest rate: %'))
    years = int(input('Enter years of accrual: '))
    print(f'Value of ${per_month} per month after 20 years at 5% interest: '
        f'${round(calculate_future_value(per_month, interest, years), 2)}')

if __name__ == '__main__':
    main()