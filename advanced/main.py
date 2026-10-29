def repeat_message_iterative(message, times):
    while times > 0:
        print(message)
        times -= 1


def repeat_message_recursive(message, times):
    # BASE CASE: times has reached 0
    if times <= 0:
        return

    # PROCESS: Print message one time
    print(message)

    # RECURSIVE STEP: Call the function again with times reduced by 1
    repeat_message_recursive(message, times - 1)


if __name__ == "__main__":
    # Ask the user for the message
    user_message = input("Enter the message to repeat: ")

    # Validate that times is a whole number that is 0 or greater
    while True:
        try:
            times_input = input("Enter how many times it should be printed (0 or greater): ")
            times_value = int(times_input)

            if times_value >= 0:
                break
            else:
                print("Error: Please enter a whole number that is 0 or greater.")
        except ValueError:
            print("Error: Invalid numeric input. Please try again.")

    print("\n--- Output ---")
    # Call the recursive function using user-provided values
    repeat_message_recursive(user_message, times_value)