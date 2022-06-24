import string

msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"


def is_num(value):
    int_marker = value.isdigit()
    float_marker = all(map(lambda num: True if num in string.digits
                                               or (num == "." and value.count(".") == 1) else False, list(value)))
    m_marker = value == "M"
    return int_marker or float_marker or m_marker


def input_validation():
    print(msg_0)
    calc = str(input()).split()
    num1, operator, num2 = calc
    if not is_num(num1) or not is_num(num2):
        print(msg_1)
        print(msg_0)
        return input_validation()
    elif operator not in {"+", "-", "*", "/"}:
        print(msg_2)
        print(msg_0)
        return input_validation()
    elif operator == "/" and num2 == "0":
        print(msg_3)
        print(msg_0)
        return input_validation()
    return calc


def operation(value, mem):
    num1, operator, num2 = value
    if num1 == "M":
        num1 = mem
    if num2 == "M":
        num2 = mem

    num1 = float(num1)
    num2 = float(num2)

    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    else:
        return num1 / num2


def branches(value):
    print(value)
    answer = str(input())
    if answer == "y":
        return True
    elif answer == "n":
        return False
    else:
        branches(value)


def program(value):
    result = operation(input_validation(), value)
    print(result)
    memory = value
    if branches(msg_4):
        memory = result
    if branches(msg_5):
        program(memory)

memory = 0
program(memory)
