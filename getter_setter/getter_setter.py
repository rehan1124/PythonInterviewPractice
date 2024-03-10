"""
https://www.youtube.com/watch?v=jCzT9XFZ5bw
"""
from dataclasses import dataclass


@dataclass
class Employee:
    first_name: str
    last_name: str

    @property
    def email(self):
        return f"{self.first_name}.{self.last_name}@email.com"

    @property
    def fullname(self):
        try:
            return f"{self.first_name} {self.last_name}"
        except AttributeError:
            return "Name has been deleted or not present. Please recheck again."

    @fullname.setter
    def fullname(self, name):
        self.first_name, self.last_name = name.split(" ")

    @fullname.deleter
    def fullname(self):
        print("Deleting fullname...")
        del self.first_name, self.last_name


def main() -> None:
    e1 = Employee("Jack", "Jil")
    print("Employee object:", e1)
    print("Email:", e1.email)
    print("Fullname:", e1.fullname)
    print("--- Changing fullname ---")
    e1.fullname = "Jane Doe"
    print("New fullname:", e1.fullname)
    print("New email:", e1.email)
    print("--- Calling deleter ---")
    del e1.fullname
    print("After fullname deletion:", e1.fullname)


if __name__ == "__main__":
    main()
