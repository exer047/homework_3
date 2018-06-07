def digit_number(value):
    digit_counter = 0
    while value >= 10:
        value /= 10
        digit_counter += 1
    return digit_counter + 1

print(digit_number(9123))