def greet(name, greeting = "Hello", repeat = 1):
    for i in range(repeat):
        print(greeting + " " + name)


greet("Ofer")
greet("Avi")
greet("David")
greet("Ofer", "Goodbye")
greet("Mori", repeat=3)

def add(a, b):
    return a + b

add(1, 2)
add(a=3, b=4)
# add(a=4, 5)  # Wrong
add(4, b=5)