# import csv

# file = open("countries.csv")
# csv_file = csv.reader(file)
# for line in csv_file:
#     print(line)
# file.close()

# file = open("countries.csv", mode="w")
# csv_file = csv.writer(file)
# csv_file.writerow(["123", "456", "abc,def"])
# file.close()

import json

my_dict = {
    "Israel": 3,
    "USA": 2,
    "Germany": 5
}

# file = open("countries.json", mode="w")
# json.dump([2, 3, "asda", 3.4, ["a", "c"]], file)
# file.close()

file = open("countries.json")
content = json.load(file)
file.close()
print(content)





