def int_input(message):
    while True:
        value = input(message)
        if value.isdigit():
            value = int(value)
            return value

def op_input(message):
    while True:
        value = input(message)
        if value in ("+", "-", "*", "/", "quit"):
            return value
        print("Wrong op, enter only one of +-*/")

result = int_input("Enter a number: ")
while True:
    op = op_input("Op: ")
    if op == "quit":
        break
    b = int_input("Enter a number: ")
    if op == "+":
        result = result + b
    elif op == "-":
        result = result - b
    elif op == "*":
        result = result * b
    elif op == "/":
        result = result / b

print(result)

##     OPTION 2: dict of functions
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

op_map = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
}

result = int_input("Enter a number: ")
while True:
    op = op_input("Op: ")
    if op == "quit":
        break
    b = int_input("Enter a number: ")
    if op in op_map.keys():
        calc = op_map[op]
        result = calc(result, b)
    else:
        print("bad")