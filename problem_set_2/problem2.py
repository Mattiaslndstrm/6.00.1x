def pay_debt_in_one_year(balance, interest):
    """Calculates the minimum monthly payment to be free of debt in one year

    Input: balance      - positive int
           interest     - annual interest in decimal form

    Output: Minimum payment as a factor of 10
    """
    payment = 10
    orig_balance = balance
    while True:
        balance = orig_balance
        for f in range(12):
            balance = (balance - payment) + interest / 12 * (balance - payment)
        if balance < 0:
            break
        payment += 10
    return payment
