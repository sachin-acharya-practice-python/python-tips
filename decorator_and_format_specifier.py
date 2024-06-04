from typing import Callable, Any
from functools import wraps
from time import sleep


def multiply_setup(prepend: int = 10) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def multiply(value: int) -> None:
            return func(prepend * value)

        return multiply

    return decorator


def retry(retries: int = 5, delay: float = 1) -> Callable:
    if retries < 1 or delay <= 0:
        raise ValueError("Fuck Off")

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            for i in range(1, retries + 1):
                try:
                    print(f"Running {i}: '{func.__name__}()'")
                    return func(*args, **kwargs)
                except Exception as e:
                    if i == retries:
                        print(
                            f"'{func.__name__}()' failed after {retries} tries with following error(s).",
                            repr(e),
                        )
                        break
                    else:
                        print("\t", repr(e))
                        sleep(delay)

        return wrapper

    return decorator


@multiply_setup(2)
def square(value: int):
    return value


@retry(retries=5, delay=1)
def retr(a: int, b: int) -> int:
    return a + b


if __name__ == "__main__":
    print("{square(20) = }")
    retr(5, 6)
    # print(f"{retr(10, 10) = }")
