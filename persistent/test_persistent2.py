"""
- Create a User
	POST https://reqres.in/api/users
	request body:  {"name": "morpheus", "job": "leader"}
	Response: {"id": "2", "createdAt": "<<date>>"}


Test1:
       Use the user id that was generated in the setup and get the user id using below GET request and validate it returns the same user id.
	GET https://reqres.in/api/users/2


Test2:
	Update the user using below request.
	PUT https://reqres.in/api/users/2
	request body: {"name": "morpheus", "job": "zion resident"}


Cleanup:
	Remove the user using below request.
	DELETE https://reqres.in/api/users/2
"""
import pytest
import requests

URL = "https://reqres.in/api/users"


@pytest.fixture()
def setup():
    payload = {"name": "morpheus", "job": "leader"}
    response = requests.post(url=URL, json=payload)
    userid = response.json()["id"]
    yield userid
    requests.delete(url=f"{URL}/{userid}")


def test_get_user(setup):
    userid = 2
    response = requests.get(url=f"{URL}/{userid}")
    json_resp = response.json()
    try:
        assert json_resp["data"]["id"] == userid
    except KeyError:
        print("Incorrect key.")

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
#
# new_fruits = [items for items in fruits if "a" in items]
# print(new_fruits)
