# list => Ordered, Mutable
my_list = [30, "hi", True, [1, 2, 4.5]]
my_list[0] = 50
print(my_list[1])
my_list.append("hello again")
my_list.remove("hi")
my_list.pop()

# tuple => Ordered, Immutable (frozen)
my_tuple = (30, "hi", True, [1, 2, 4.5])
# my_tuple[0] = 50  # Error
print(my_tuple[1])

# set => Unordered, Mutable, Unique values
my_set = {30, "hi", True}
my_set = {(1, 3), (1, 2), 3}
my_set.add(5)
my_set.remove(3)


my_list = ["a", "b", "c"]
index = 0
while index < len(my_list):
    print(my_list[index])
    index = index + 1

for letter in my_list:
    print(letter)

for letter in my_tuple:
    print(letter)

my_set = {"a", "b", "c"}
for letter in my_set:
    print(letter)

for letter in "how are you":
    print(letter)

# dict => Unordered, Mutable, Unique keys
user = {"password": "1234", "age": 40, "children": 2}
user["name"] = "Ofer"
print(user["name"])
for pair in user.values():
    print(pair)

user = {}
user["name"] = input("Enter name: ")
user["age"] = input("Enter age: ")
has_children = input("Do you have children? (Y/N) ")
if has_children == "Y":
    user["children"] = input("How many children: ")

output = user["name"] + " is " + user["age"] + " years old" + " and has " + user.get("children", "0") + " children"
print(output)

user = {
    "name": "Ofer",
    "age": 40,
    "children": ["david", "yosef", "maya"]
}

# Solution 1
user = {}
user["name"] = input("Enter name: ")
user["age"] = input("Enter age: ")
user["children"] = []
number_children = int(input("How many children? "))
for i in range(number_children):
    child = input("Name: ")
    user["children"].append(child)

# Solution 2
user = {}
user["name"] = input("Enter name: ")
user["age"] = input("Enter age: ")
user["children"] = []
child = ""
while child != "quit":
    child = input("Name: ")
    user["children"].append(child)
user["children"].pop()

output = user["name"] + " is " + user["age"] + " years old" + " and has " + str(len(user["children"])) + " children"
for child in user["children"]:
    output += " " + child
print(output)
