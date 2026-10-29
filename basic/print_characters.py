def print_characters_recursive(text, position):
    # BASE CASE: index reaches or exceeds the length of the text
    if position == len(text):
        return
    # PROCESS: print the character at the current index
    print(text[position])
    # RECURSIVE STEP: move closer to the base case by incrementing the index
    print_characters_recursive(text, position + 1)


print_characters_recursive("robot", 0)

def print_characters_iterative(text):
    pass