def print_three(word1, word2):
    for i in range(3):
        print(word1 + word1 + word2)

def add(a, b):
    total = a + b
    return total

x = add(2, 3.5)
print(x)

def int_input(message):
    while True:
        value = input(message)
        if value.isdigit():
            value = int(value)
            return value


number = int_input("Please enter a number: ")
print(type(number))
print(number)

print(int_input)
