import pathlib

def load_data(path: pathlib.Path | str) -> dict:
    """Load data from a file to a dict"""
    with open(path) as file:
        data = {}  # dict()
        for line in file:
            line = line.strip().split(": ")
            key = line[0]
            value = int(line[1])
            data[key] = value
    return data

def multiply_data(data: dict[str, int]):
    # {'Israel': 3, 'USA': 2, 'Germany': 1}
    # for key in data:
    #     data[key] = data[key] * 2
    for key, value in data.items():
        data[key] = value * 2
    # return data


def save_data(data: dict, path: pathlib.Path | str):
    # {'Israel': 6, 'USA': 4, 'Germany': 2}
    with open(path, mode="w") as file:
        for key, value in data.items():
            line = key + ": " + str(value) + "\n"
            file.write(line)


path = pathlib.Path("cities.txt")
data = load_data(path)
print(data)
multiply_data(data)  # No need # data = multiply_data(data)
print(data)
save_data(data, path)
