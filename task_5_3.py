def print_rhombus(n):
    point_counter = 1
    while point_counter < n:
        print(int((n - point_counter) / 2) * " ", point_counter * "*", int((n - point_counter) / 2) * " ")
        point_counter += 2
    while point_counter >= 1:
        print(int((n - point_counter) / 2) * " ", point_counter * "*", int((n - point_counter) / 2) * " ")
        point_counter -= 2

print_rhombus(5)