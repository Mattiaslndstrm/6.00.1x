from string import ascii_lowercase as alphabet


# First try
def longest_alphabetic_substring(s):
    total = ''
    strings = []
    previous = 0
    for f in s:
        position = alphabet.index(f)
        if position >= previous:
            total += f
            previous = position
        else:
            strings.append(total)
            total = f
            previous = position
    strings.append(total)
    return max(strings, key=lambda a: len(a))


# Second try while being inspired by other ideas, but not stealing
def longest_alphabetic_substring2(s):
    total = previous = ''
    strings = []
    for char in s:
        if char >= previous:
            total += char
            previous = char
        else:
            strings.append(total)
            total, previous = char, char
    return max((*strings, total), key=len)


# Third try, 'copying' a censored 9 liner from the course forum
def longest_alphabetic_substring3(s):
    current = longest = ''
    for char in s:
        if current and char > current[-1]:
            if len(current) > len(longest):
                longest = current
            current += char
        else:
            current = char
    return longest


print(longest_alphabetic_substring3('abcdefghijklmnopqrstuvwxyz'))
print('abc'>'aba')