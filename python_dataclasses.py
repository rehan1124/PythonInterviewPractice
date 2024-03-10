"""
Python dataclasses

https://www.youtube.com/watch?v=CvQ7e6yUtnw
"""
from dataclasses import dataclass, field
import uuid


def generate_random_id():
    return str(uuid.uuid4())


@dataclass(frozen=True)
class Person:
    name: str
    age: int
    active: bool = True
    id: int = field(init=False, default_factory=generate_random_id)


def main() -> None:
    p1 = Person("Jack", 30)
    print(p1)


if __name__ == "__main__":
    main()
