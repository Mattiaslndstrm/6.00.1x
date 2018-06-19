# Readable, simple solution
def count_bob(s):
    """
    Write a program that prints the number of
    times the string 'bob' occurs in s.
    """
    total = 0
    for f in range(0, len(s)):
        if s[f:f + 3] == 'bob':
            total += 1
    return 'Number of times bob occurs is: ' + str(total)


# Much less readable, but short.
def count_bob2(s):
    """
    Write a program that prints the number of
    times the string 'bob' occurs in s.
    """
    return ('Number of times bob occurs is: ' + str(
        len([s[f:f + 3] for f in range(0, len(s)) if s[f:f + 3] == 'bob'])))
