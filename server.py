from flask import Flask, request, Response

app = Flask("myapp")

def search_user_by_id(search_id: int | None, users_data: list) -> dict | list | None:
    if search_id is not None:
        # search_id = int(search_id)
        for user in users_data:
            if user["id"] == search_id:
                return user
        return None
    return users_data


@app.route("/users")
def get_users():
    users_data = [{"id": 1, "name": "Ofer"}, {"id": 2, "name": "Avi"}]
    # user_agent = request.headers["User-Agent"]
    user_agent = request.headers.get("User-Agent", "")
    search_id = request.args.get("id", None, type=int)
    if "curl" in user_agent:
        data = search_user_by_id(search_id, users_data)
        if data is None:
            return "Error not found", 404
        return data
    else:
        # return Response("We only support curl", 400)
        # return Response("We only support curl", status=400)
        # return ("We only support curl", 400)
        return "We only support curl", 400


@app.route("/users/<int:user_id>")
def get_user_by_id(user_id: int):
    # user_id = int(user_id)
    users_data = [{"id": 1, "name": "Ofer"}, {"id": 2, "name": "Avi"}]
    data = search_user_by_id(user_id, users_data)
    if data is None:
        return "Error not found", 404
    return data


# curl localhost:8888/users
# curl localhost:8888/users?id=1
# curl localhost:8888/users?id=2
# curl localhost:8888/users?id=3  # 404 error

# curl localhost:8888/users/1
# curl localhost:8888/users/2
# curl localhost:8888/users/3  # 404 error


app.run("0.0.0.0", 8888)
