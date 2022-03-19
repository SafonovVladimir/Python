def upper_lower_string(s):
    if ' ' in s:
        return s.upper()
    else:
        return s.lower()


# s = input('Введіть будь-яку строку: ')
print(upper_lower_string('sdfasdf gfjh'))
print(upper_lower_string('sdFSsdf,gfjh'))
print(upper_lower_string('sdfasdfgfjh'))
