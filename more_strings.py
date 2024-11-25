name = input('Введіть своє ім`я ') + '\n\n'
# age = input('Введіть свій вік ')


name = name.title()
name = name.strip()
name = name.strip('0123456789 ')
# name = name.lstrip('0123456789 ')
# name = name.rstrip('0123456789 ')
# name = name.lower()
# name = name.upper()

name = name.title().strip('0123456789 ')
name = name.replace('ff', '!', 2)
name = name.capitalize()

multiplication = '*' * 50
print(multiplication)

print(name)
