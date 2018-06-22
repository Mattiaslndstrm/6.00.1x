def balance_after_months(balance, interest, monthly_rate, months=12):
    """Calculate the remaining balance on a loan after n months

    Input: balance      - a positive int
           interest     - annual interest rate in decimal form
           monthly_rate - minimum monthly payment, in percent of remaining
                          payment, in decimal form. Default = 12

    Output: remaining balance after n months, rounded to two decimals
    """
    if months == 0:
        return round(balance, 2)
    balance = balance - monthly_rate * balance
    balance = balance + balance * (interest / 12)

    return balance_after_months(balance, interest, monthly_rate, months - 1)
