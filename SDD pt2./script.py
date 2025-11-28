def add_char(input_str, character):
    if not input_str or input_str == "0":
        return character
    else:
        return input_str + character

import math

def cos(value):
    return math.cos(value)

def sin(value):
    return math.sin(value)

def tan(value):
    return math.tan(value)

def sqrt(value):
    return math.sqrt(value)

def ln(value):
    return math.log(value)

def exp(value):
    return math.exp(value)

def delete_char(input_str):
    return input_str[:-1]

val = 0.0
def percent(input_str):
    global val
    val = float(input_str)
    return input_str + "%"

def change_sign(input_str):
    if input_str.startswith("-"):
        return input_str[1:]
    else:
        if input_str == "0":
            return input_str[0:]
        else:
            return "-" + input_str


def compute(input_str):
    global val
    #if val != 0.0:
    #    percent_val = float(input_str.replace("%", ""))
    #    input_str = str(percent_val / 100 * val)
    #    val = 0.0
    try:
        result = eval(input_str)
        return str(result)
    except Exception as e:
        print(f"Error: {e}")
        return input_str

def square(value):
    return value * value

def check_num(input_str):
    allowed_chars = set("0123456789/.+-*()%")
    if set(input_str) <= allowed_chars:
        return True
    else:
        print("Invalid entry!")
        return False