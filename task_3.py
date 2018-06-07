def is_even(value):
    if value % 2 == 0:
        return True
    else:
        return False

even_count = 0
iterator = 0
n = int(input("Enter n: "))
while even_count < n:
    if is_even(iterator):
        even_count += 1
        print(iterator)
    iterator += 1


