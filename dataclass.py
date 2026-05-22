from dataclasses import dataclass

@dataclass(frozen = True)
class Person:
    name: str
    age: int
    #password: str = field(repr = False)
    is_alive: bool= True

    def __post_init__(self):
        if self.age<0:
            raise ValueError("Age cannot be negative")

person1 = Person("SBoB", 12)
person2 = Person("Lizz", 15)

print(person1)
print(person2)
print(person1==person2)