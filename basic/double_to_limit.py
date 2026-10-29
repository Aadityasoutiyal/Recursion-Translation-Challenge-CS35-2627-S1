def double_until_limit_recursive(number, limit):
    # BASE CASE: number exceeds the limit
    if number > limit:
        return
    # PROCESS: print the current number
    print(number)
    # RECURSIVE STEP: move closer to the base case by doubling the number
    double_until_limit_recursive(number * 2, limit)


double_until_limit_recursive(2, 40)

def double_until_limit_iterative(number, limit):
    pass