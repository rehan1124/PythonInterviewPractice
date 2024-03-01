# import json
#
#
# def create_json_object(**kwargs):
#     return json.dumps(kwargs), kwargs.get("last_name")
#
#
# print(create_json_object(first_name="Rehan", last_name="Rehan"))
#
# try:
#     infile = open("file.txt", "r")
#     infile.readlines()
# except Exception as e:
#     print(e)
# finally:
#     infile.close()

from abc import ABC, abstractmethod


class Browser(ABC):
    @abstractmethod
    def open_browser(self):
        pass


class Chrome(Browser):
    def open_browser(self):
        print("Running tests in Chrome.")


class Firefox(Browser):
    def open_browser(self):
        print("Running tests in Firefox.")
