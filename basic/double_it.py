def handlePrompt():
    try:
        user_input = int(input("Enter value to double it: "))
        if user_input == 0:
            print("input value cannot be zero.")
        else:
            curr_value = user_input
            while curr_value < 100:
                print(curr_value)
                curr_value = curr_value * 2
            print(curr_value)

    except ValueError:
        print("input must be an integer")

handlePrompt()
