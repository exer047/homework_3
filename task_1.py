def is_prime(a):
    divider_counter = 0
    for i in range(a):
        divider_check = a % (i + 1)
        if divider_check == 0:
            divider_counter += 1
    if divider_counter > 2:
        return False
    else:
        return True



print(is_prime(23))