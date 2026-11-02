# int
x = 5
# float
x = 4.4
# str
x = "hello world"
# bool
x = True
y = False
# None
x = None

# if x > 10:
#     print("hi")
# else:
#     print("bye")

# while True:
#     print("forever")
#     if x < 5:
#         break

# while x < 10:
#     print("sometimes")

for i in range(10):
    print(i)
    if x == 5:
        break

print("hello")
s = input("please write")
x = len(s)
x = [1, 2, 3]
total = sum(x)

int("123")
int("abc")  # error
float("123")
float(123)
bool("")  # False
bool("hello")  # True
bool(0)  # False
bool(123)  # True

name = "ofer"
if name == "maya" or name == "ofer":
    print("hi there")

# while name == "maya" or "ofer":
#     print("hi again")

name = "ofer"
has_letter_a = "er" in name
print(name[0])
last = "sadan"
full = name + last
full = full.upper()

s = "fhkah"
s = 'adsd'
s = "Don't"
s = 'Ofer said "Hi"'
