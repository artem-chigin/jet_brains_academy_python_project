import string

msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"
msg_ = ["", msg_1, msg_2, msg_3, msg_4, msg_5, msg_6, msg_7, msg_8, msg_9, msg_10, msg_11, msg_12]


def is_num(value):
    if type(value) == int or type(value) == float:
        return True
    else:
        int_marker = value.isdigit()
        float_marker = all(map(lambda num: True if num in string.digits
                                                or (num == "." and value.count(".") == 1) else False, list(value)))
        m_marker = value == "M"
        return int_marker or float_marker or m_marker


def input_and_validation(mem):
    print(msg_0)
    calc = str(input()).split()
    calc = list(map(lambda x: x if x != "M" else str(mem), calc))
    num1, operator, num2 = calc

    check(num1, num2, operator)

    if not is_num(num1) or not is_num(num2):
        print(msg_1)
        return input_and_validation(mem)
    elif operator not in {"+", "-", "*", "/"}:
        print(msg_2)
        return input_and_validation(mem)
    elif operator == "/" and (num2 == "0" or num2 == "0.0"):
        print(msg_3)
        return input_and_validation(mem)

    return calc


def is_one_digit(value):
    if -10 < float(value) < 10 and float(value).is_integer():
        return True
    else:
        return False


def check(v1, v2, v3):
    msg = ""
    # print(v1, v2, v3)
    if is_one_digit(v1) and is_one_digit(v2):
        msg = msg + msg_6

    if (v1 == "1" or v2 == "1") and v3 == "*":
        msg = msg + msg_7
    if (v1 == "0.0" or v1 == "0" or v2 == "0.0" or v2 == "0") and (v3 == "+" or v3 == "-" or v3 == "*"):
        msg = msg + msg_8
    if msg != "":
        msg = msg_9 + msg
        print(msg)


def operation(value):
    num1, operator, num2 = value

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


def memory(result_value, old_memory_value):
    memory_value = str(result_value)
    if is_one_digit(memory_value):
        msg_index = 10
        while msg_index <= 12:
            if branches(msg_[msg_index]):
                msg_index += 1
            else:
                return old_memory_value
        return memory_value

    else:
        return memory_value


def program(memory_value="0.0"):
    result = operation(input_and_validation(memory_value))
    print(result)
    mem = memory_value
    if branches(msg_4):
        mem = memory(str(result), mem)
        # print(memory)
    if branches(msg_5):
        program(mem)


program()
