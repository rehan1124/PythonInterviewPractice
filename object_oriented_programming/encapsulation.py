"""
https://www.youtube.com/watch?v=fjIUS1jlVkA

https://www.youtube.com/playlist?list=PLdo5W4Nhv31bZSiqiOL5ta39vSnBxpOPT Full python course
"""
from dataclasses import dataclass


@dataclass
class Student:
    name: str  # Public
    _rollno: int  # Protected
    __age: int  # Private

    @property
    def rollno(self) -> int:
        """

        Returns:

        """
        return self._rollno

    @rollno.setter
    def rollno(self, value):
        self._rollno = value

    @property
    def age(self) -> int:
        """

        Returns:

        """
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value

    def details(self) -> str:
        return f"Hi! My name is {self.name}, roll number: {self.rollno}, age: {self.age}"


def main():
    s1 = Student("John", 11, 18)
    print("Complete object:", s1)
    print("Roll number:", s1.rollno)
    print("Age:", s1.age)
    print(s1.details())


if __name__ == "__main__":
    main()
