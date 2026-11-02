import pathlib

# p_linux = "/home/liran/python-example/test55/countries.txt"
# p_windows = "C:\\Users\\ofer\\1.txt"
# print(pathlib.Path.home())  # User's home dir
# print(pathlib.Path.cwd())  # Current working dir

# special_file = pathlib.Path.home() / "1.txt"
# print(special_file)
# all_users_home = pathlib.Path.home().parent
# print(all_users_home)
# countries = pathlib.Path("/home/liran/python-example/test55/countries.txt")
# print(countries.suffix)
# dir = pathlib.Path.home() / "my_special_test"
# dir.mkdir()

current_script = pathlib.Path(__file__)
countries_path = current_script.with_name("countries.txt")

file = open(countries_path)
countries = set()
for line in file:
    countries.add(line.strip().capitalize())

# countries = sorted(countries)
# print(countries)

countries = list(countries)
countries.sort()
print(len(countries))
for country in countries:
    print(country)

file.close()


import pathlib

# new_file_path = pathlib.Path("cities.txt")
# new_file = open(new_file_path, mode="w")
# new_file = new_file_path.open()

# new_file.write("Hello")
# new_file.write("\n")
# new_file.write("World")

# new_file.write("Hello\nWorld")

# new_file.writelines(["Hello", "\n", "World"])

# print("Hello", file=new_file)
# print("World", file=new_file)

file_path = pathlib.Path("cities.txt")

def file_to_dict():
    new_file = open(file_path)
    countries = {}
    for line in new_file:
        # "Israel: 3\n"
        line = line.split()
        # ["Israel:", "3\n"]
        country = line[0].strip(":")
        number = int(line[1].strip())
        countries[country] = number
    return countries

def dict_max(some_dict):
    max_points = max(some_dict.values())
    for key, value in some_dict.items():
        if value == max_points:
            return key

def dict_to_file(some_dict, some_file):
    for key, value in some_dict.items():
        some_file.write(key + ": " + str(value) + "\n")


my_dict = {
    "Israel": 3,
    "USA": 2,
    "Germany": 5
}

