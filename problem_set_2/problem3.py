def pay_debt_in_one_year(balance, interest, _upper=0, _lower=0):
    """Calculates the minimum monthly payment to be free of debt in one year

    Input: balance      - positive int
           interest     - annual interest in decimal form
           _upper       - for internal use
           _lower       - for internal use

    Output: Minimum payment as a factor of 0.01
    """

    # Sets _upper to be 1/12 of the compunded total when the monthly interest
    # rate is applied every month without payment. _lower is set to 1/12 of the
    # original balance
    if not _upper and not _lower:
        _upper = balance * ((1 + interest / 12) ** 12) / 12
        _lower = balance / 12

    # guess is the average of _lower and _upper
    guess = (_lower + _upper) / 2
    orig_balance = balance

    for _ in range(12):
        balance = (balance - guess) + interest / 12 * (balance - guess)

    # returns the guess when it's inside the margin of error
    if balance <= 0 and balance > -0.01:
        return round(guess, 2)
    # Bidirectional search. Recursively returns _lower set to guess if the
    # guess was too low, and _upper set to guess if the guess was too high.
    if balance < -0.01:
        return pay_debt_in_one_year(orig_balance, interest, guess, _lower)
    return pay_debt_in_one_year(orig_balance, interest, _upper, guess)
