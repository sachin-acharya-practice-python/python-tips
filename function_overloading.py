from multipledispatch import dispatch  # pip install multipledispatch


@dispatch(int, int)
def add(a: int, b: int):
    return a + b


@dispatch(str, str)
def add(a: str, b: str):
    return a + " " + b


print("With int, int -> 10, 20")
print(add(10, 10))

print("With str, str -> Hello, World")
print(add("Hello", "World"))