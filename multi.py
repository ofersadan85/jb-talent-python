import time
import json
import requests
from pathlib import Path
import threading

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
    print("Saved", filename)

start = time.perf_counter()


my_cool_threads = []
for i in range(1, 11):
    t = threading.Thread(target=download_user, args=[i])
    # t = threading.Thread(target=download_user, kwargs={"user_id": i})
    t.start()
    my_cool_threads.append(t)

for t in my_cool_threads:
    t.join()
    

end = time.perf_counter()
print(end - start)






# import time
# import threading

# QUIT = []
# NUM_LIST = [0]

# list_lock = threading.Lock()

# def count():
#     i = 0
#     while not QUIT:
#         list_lock.acquire()
#         last_item = NUM_LIST[-1]
#         time.sleep(1)
#         NUM_LIST.append(last_item + 1)
#         list_lock.release()
#         i += 1
#     print("FINISHED")
#     print(NUM_LIST)


# def double_input():
#     while True:
#         x = input()
#         if x == "quit":
#             QUIT.append(None)
#             break
#         print(x * 2)

# t1 = threading.Thread(target=double_input)
# for i in range(10):
#     t = threading.Thread(target=count)
#     t.start()

# t1.start()

