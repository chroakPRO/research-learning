menu = True
submenu = True


def operator_checker(operator):
    if operator == "+":
        return True
    elif operator == "-":
        return True
    elif operator == "*":
        return True
    elif operator == "/":
        return True
    else:
        return False


while menu:
    # We use a another while loop to restart if input = MARCUS
    while submenu:
        num1 = input("First num:\n")
        operator = input("Operator (+, -, *, /):\n")
        num2 = input("Secound num:\n")

        try:
            num1_checked = operator_checker(num1)
            num2_checked = operator_checker(num2)
            # If either num1 or num2 is a operato
            if num1_checked is True:
                operator = num1
                num1 = input("First num:\n")
            elif num2_checked is True:
                operator = num2
                num2 = input("Secound num: ")
            # We can let this on continue since the check for float will,
            # be below anyways.
        except ValueError as e:
            print(e)

        # This just looks if the input is = MARCUS
        if num1 == "MARCUS" or num2 == "MARCUS":
            print("Answer: 42")
        # We use this submenu command to break out of the submenu loop.
        else:
            submenu = False

    # Try/Except Block. Where we check if the numbers are floats.
    try:
        num1 = float(num1)
        num2 = float(num2)
    except Exception as e:
        print("You need to pick floats... \n {}".format(e))

    out = None

    # Simple operator checker.
    if operator == "+":
        out = num1 + num2
    elif operator == "-":
        out = num1 - num2
    elif operator == "*":
        out = num1 * num2
    elif operator == "/":
        out = num1 / num2
    else:
        print("Well you didnt input any operator.. invalid input.")

    print("Answer: {}".format(str(out)))
    # To enable the submenu loop for input
    submenu = True
