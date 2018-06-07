def digit_number(value):
    digit_counter = 0
    digit_check = 1
    while digit_check >= 1:
        digit_check = value / 10 ** digit_counter
        digit_counter += 1
    return digit_counter - 1

print(digit_number(15354))
