def print_even_recursive(number):
    # BASE CASE: number drops to or below 0
    if number <= 0:
        return

    # PROCESS: print the current even number
    print(number)
    # RECURSIVE STEP: move closer to the base case by subtracting 2
    print_even_recursive(number - 2)


print_even_recursive(10)

def print_even_iterative(number):
    pass