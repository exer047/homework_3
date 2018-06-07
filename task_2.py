def is_prime(a):
    divider_counter = 0
    for i in range(a):
        divider_check = a % (i + 1)
        if divider_check == 0:
            divider_counter += 1
    if divider_counter == 2:
        return True
    else:
        return False

prime_count = 0
n = int(input("Type n: "))
iterator = 1
while prime_count < n:
    if is_prime(iterator):
        prime_count += 1
        print(iterator)
    iterator += 1


