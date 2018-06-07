def my_len(value):
    counter = 0
    for value in value:
        counter += 1
    return counter


print(len('hello'))
print(my_len('hello'))

print(len([1,2,3,4,5]))
print(my_len([1,2,3,4,5]))