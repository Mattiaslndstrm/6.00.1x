# Python < 3.6
def vowels(s):
    return 'Number of vowels: {}'.format(len([f for f in s if f in 'aeiou']))
print(vowels(s))


# Python 3.6+
def vowels(s):
    return f'Number of vowels: {len([f for f in s if f in "aeiou"])}'
print(vowels(s))
