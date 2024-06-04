class User:
    def __init__(self):
        self._name: str = ""
        self._age: int = 0
        self._hobbies: str = ""

    def get_name(self):
        print("Getter -> Name")
        return self._name

    def set_name(self, name: str):
        print("Setter -> Name")
        self._name = name

    def get_age(self):
        print("Getter -> Age")
        return self._age

    def set_age(self, age: int):
        print("Setter -> Age")
        self._age = age

    def get_hobbies(self) -> str | None:
        print("Getter -> Hobbies")
        if self._hobbies:
            return self._hobbies
        return None

    def set_hobbies(self, hobbies: list[str]):
        print("Setter -> Hobbies")
        self._hobbies = "; ".join(hobbies)

    def del_hobbies(self):
        print("Delete -> Hobbies")
        del self._hobbies

    name = property(get_name, set_name)
    age = property(get_age, set_age)
    hobbies = property(get_hobbies, set_hobbies, del_hobbies)


new_user = User()
print("Assigning")
print("----------------------------------------------------------")
new_user.name = "Sachin Acharya"
new_user.age = 24
new_user.hobbies = ["Singing", "Coding", "Eating", "Reading"]

print("\nAccessing")
print("----------------------------------------------------------")
print("Name", new_user.name)
print("Age", new_user.age)
print("Hobbies", new_user.hobbies)

print("\nDeleting")
print("----------------------------------------------------------")
del new_user.hobbies


class Person:
    def __init__(self, name: str, age: int) -> None:
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age: int):
        self._age = age


print("\nPerson Class\n")
p = Person("Guest", 10)
print(p.name)
p.name = "Sachin Acharya"

print(p.age)
p.age = 24

print(p.name, p.age)