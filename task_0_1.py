def factorial(value):
    result = 1
    for i in range(value):
        result = result * (i + 1)
    return result

print(factorial(5))
