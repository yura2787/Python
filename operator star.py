def multiply(*args):
    result = 1
    for number in args:
       result *= number
    return result

print(multiply(2, 3, 4))
print(multiply(5, 6))
