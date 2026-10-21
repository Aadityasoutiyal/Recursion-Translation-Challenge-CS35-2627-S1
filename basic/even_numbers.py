def print_even_recursive(number):
    if number <= 0:
        return

    print(number)

    print_even_recursive(number - 2)


print_even_recursive(10)

def print_even_iterative(number):
    pass