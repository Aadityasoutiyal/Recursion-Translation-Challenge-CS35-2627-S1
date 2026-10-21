def double_until_limit_recursive(number, limit):
    if number > limit:
        return

    print(number)

    double_until_limit_recursive(number * 2, limit)


double_until_limit_recursive(2, 40)

def double_until_limit_iterative(number, limit):
    pass