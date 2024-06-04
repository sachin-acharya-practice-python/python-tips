from dataclasses import dataclass, fields
from typing import Literal
from functools import lru_cache
import time


@dataclass(slots=True, frozen=True, repr=True)
class Person:
    name: str
    age: int
    address: str
    phone: str

    @lru_cache
    def __getitem__(self, key):
        time.sleep(3)
        for field in fields(self):
            if field.name == key:
                return getattr(self, key)
        raise KeyError(f"{key} not found.")

    def get(
        self,
        key: Literal["name", "age", "address", "phone"],
        default: str | None = None,
    ):
        try:
            return self[key]
        except KeyError:
            return default


p = Person("Sachin Acharya", 34, "Address", 123456767)
print(f"{p['name'] = }")
print(f"{p.get('name', None) = }")
