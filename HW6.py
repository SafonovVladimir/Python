def upper_lower_string(s):
    if ' ' in s:
        s = s.upper()
    else:
        s = s.lower()
    return s


s = input('Введіть будь-яку строку: ')
print(upper_lower_string(s))
