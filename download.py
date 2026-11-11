import requests
import urllib.request
from pathlib import Path


def download_file_std(url: str, filename: str | Path, chunk_size: int = 1024) -> int:
    # sending_content = b"wow"
    # headers = {
    #     "Host": "www.google.com",
    #     "User-Agent": "Mozilla/5.0",
    #     "Accept": "application/json",
    # }
    # req = urllib.request.Request(url, data=sending_content, headers=headers, method="POST")
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        print("Status:", response.status)
        if response.status != 200:
            return 0
        print("Headers:", response.headers)
        final_size = response.headers.get("Content-Length", "Unknown")
        print("Downloading", final_size, "bytes", type(final_size))
        with open(filename, mode="wb") as file:
            # content = response.read()
            size = 0
            while True:
                chunk = response.read(chunk_size)
                # if chunk == b"":
                if not chunk:
                    break
                n = file.write(chunk)
                size += n
                print(size, end="\r")
    print()
    return size

def download_file_requests(url: str, filename: str | Path) -> int:
    response = requests.get(url)
    # content = response.content  # bytes
    # text = response.text  # str
    # data = response.json()  # any JSON type
    if response.status_code == 200:
        with open(filename, mode="wb") as file:
            size = file.write(response.content)
            return size
    return 0

from pathlib import Path
import json
import requests

def download_all_users():
    url = "https://jsonplaceholder.typicode.com/users"

    response = requests.get(url)
    print(response)
    if response.status_code == 200:
        users = response.json()

    users_folder = Path("users")
    users_folder.mkdir(exist_ok=True)

    for user in users:
        # filename = str(user["id"]) + " - " + user["name"] + ".json"
        filename = f"{user['id']} - {user['name']}.json"
        filename = users_folder / filename
        with open(filename, "w") as file:
            json.dump(user, file, indent=4)

def download_one_by_one():
    users_folder = Path("users")
    users_folder.mkdir(exist_ok=True)

    user_id = 1
    while True:
        url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
        response = requests.get(url)
        if response.status_code != 200:
            break
        user = response.json()
        filename = f"{user['id']} - {user['name']}.json"
        filename = users_folder / filename
        with open(filename, "w") as file:
            json.dump(user, file, indent=4)
        print("Saved", filename)
        user_id += 1


download_one_by_one()
print("******")
download_all_users()
print("******")

url = "https://hips.hearstapps.com/hmg-prod/images/gettyimages-180680638-676f621f720bc.jpg"
size = download_file_std(url, "dogs.jpg", 2048)
# size = download_file_requests(url, "dogs.jpg")
print("Downloaded", size, "bytes")


# response = requests.post(url, data="something")
# import json
# new_user_str = json.dumps(new_user)
# response = requests.post(url, data=new_user_str, headers={"Content-Type": "application/json"})
# response = requests.post(url, json=new_post)
