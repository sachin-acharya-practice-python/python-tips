from types import UnionType
from typing import Self, Any, Literal
import re


class Fruit:
    def __init__(self, name: str, price: float, inventory_amount: float) -> None:
        self.name = name
        self.price = price
        self.inventory_amount = inventory_amount

    def __add__(self, value: Self) -> Self:
        self.inventory_amount += value.inventory_amount
        return self

    def __sub__(self, value: Self) -> Self:
        self.inventory_amount -= value.inventory_amount
        return self

    def __mul__(self, value: Self) -> Self:
        self.price *= value.price
        self.inventory_amount *= value.inventory_amount

        return self

    def __eq__(self, value: Self) -> bool:
        # ? Trigget when equility operator (=) is used.
        return (self.name == value.name) and (self.price == value.price)

    def __gt__(self, value: Self) -> bool:
        # ? Trigger when > or < is used
        return self.inventory_amount > value.inventory_amount

    def __or__(self, value: Self) -> Self:
        # ? Trigger when '|' is used
        if self.name == value.name:
            self.price += value.price
            self.inventory_amount += value.inventory_amount
        return self

    def __and__(self, value: Self) -> Self:
        # ? Trigger when '&' is used
        if self.name == value.name:
            self.price *= value.price
            self.inventory_amount *= value.inventory_amount
        return self

    def __format__(self, format_spec: str) -> str:
        # ? Used with formated string
        final_string = format_spec
        pattern = r"(?<=%)[a-zA-Z]"
        matches = re.findall(pattern, format_spec)

        for match_ in matches:
            match match_:
                case "n":
                    final_string = final_string.replace("%n", self.name, 1)
                case "p":
                    final_string = final_string.replace("%p", f"{self.price}", 1)
                case "i":
                    final_string = final_string.replace(
                        r"%i", f"{self.inventory_amount}", 1
                    )
                case _:
                    raise ValueError(f"Invalid Format Specifier '%{match_}'")
        return final_string

    def __getitem__(self, key: Literal["name", "price", "inventory_amount"]) -> Any:
        # Used with ['attribute'] method
        match key:
            case "name":
                return self.name
            case "price":
                return self.price
            case "inventory_amount":
                return self.inventory_amount
            case _:
                raise ValueError(
                    "%s doesn't have attribute '%s'" % (self.__class__.__name__, key)
                )

    def __enter__(self, *args, **kwargs) -> Self:
        # Trigger when 'with' statement starts
        print("'Enter' executed")
        return self

    def __exit__(self, *args, **kwargs) -> None:
        # Trigger when 'with' statement terminate
        print("'Exit' executed")
        return None

    def __repr__(self) -> str:
        # When repr() method is called
        return f"REPR: {self.__class__.__name__}(name={repr(self.name)}, price={repr(self.price)}, inventory_amount={repr(self.inventory_amount)})"

    def __str__(self) -> str:
        # When str() method is called
        return f"STR: {self.__class__.__name__}(name={repr(self.name)}, price={repr(self.price)}, inventory_amount={repr(self.inventory_amount)})"


if __name__ == "__main__":
    apple = Fruit("Apple", 23.0, 50.2)
    banana = Fruit("Banana", 30, 40.2)
    orange = Fruit("Orange", 23.0, 50.2)
    apple_small = Fruit("Apple", 23.0, 66)

    print("Equility Operator")
    print(f"{(apple == banana) = }")
    print(f"{(apple == orange) = }")
    print(f"{(banana == orange) = }")
    print(f"{(apple == apple_small) = }")

    print("\n\nLess than (<)")
    print(f"{(apple < banana) = }")
    print(f"{(apple < apple_small) = }")
    print(f"{(apple < orange) = }")
    print(f"{(banana < orange) = }")

    print("\n\nGreated than (>)")
    print(f"{(apple > banana) = }")
    print(f"{(apple > apple_small) = }")
    print(f"{(apple > orange) = }")
    print(f"{(banana > orange) = }")

    print("\n\nFormat Specifier")
    print(f"%n per %p with quantity %i kilo = {apple:%n per %p with quantity %i kilo}")

    print("\n\nLogical + operator")
    print(f"{(apple + apple_small) = }")

    print("\n\nLogical - operator")
    print(f"{(apple - apple_small) = }")

    print("\n\nLogical * operator")
    print(f"{(apple * apple_small) = }")

    print("\n\nLogical OR '|' operator")
    print(f"{(apple | apple_small) = }")

    print("\n\nLogical AND operator")
    print(f"{(apple & apple_small) = }")

    print("\n\nBox attribute selection")
    print(f"{apple['name'] = }")
    print(f"{apple['price'] = }")
    print(f"{apple['inventory_amount'] = }")

    print("\n\nWith statement")
    with Fruit("Apple", 23.0, 223.1) as apple:
        print(f"{apple = }")
