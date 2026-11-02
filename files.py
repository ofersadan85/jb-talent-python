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
