import time
import json
import requests
from pathlib import Path
import threading
import queue

def download_user(user_id: int):
    users_folder = Path("users")
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    response = requests.get(url)
    if response.status_code != 200:
        return
    user = response.json()
    filename = f"{user['id']} - {user['name']}.json"
    filename = users_folder / filename
    with open(filename, "w") as file:
        json.dump(user, file, indent=4)
    print(threading.current_thread().name, "Saved", filename)

user_queue = queue.Queue()
for i in range(1, 11):
    user_queue.put(i)
# user_ids_to_download = [1, 2, 3, 4, 5, 6 ,7 ,8 ,9, 10]

def worker():
    while True:
        item = user_queue.get()
        download_user(item)
        user_queue.task_done()

for i in range(3):
    t = threading.Thread(target=worker, daemon=True)
    t.start()

print("BEFORE JOIN")
user_queue.join()
print("AFTER JOIN")
