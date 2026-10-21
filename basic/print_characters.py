def print_characters_recursive(text, position):
    if position == len(text):
        return

    print(text[position])

    print_characters_recursive(text, position + 1)


print_characters_recursive("robot", 0)

def print_characters_iterative(text):
    pass