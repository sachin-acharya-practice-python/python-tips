from multipledispatch import dispatch
from typing import Generator, Any

def __range(start: int, end: int, step: int = 1):
    i = start
    while i < end:
        yield i
        i += step
    yield i

@dispatch(int, int | None)
def step(end: int, step: int = 1) -> Generator[int, Any, None]:
    """Generate iterables of number upto certain value

    Args:
        end (int): Value upto which iterable is to generate
        step (int, optional): Increment value, to increase every subsequent value. Defaults to 1.

    Yields:
        Generator[int, Any, None]: Generator of iterables
    """
    return __range(1, end, step)

@dispatch(int, int, int | None)
def step(start: int, end: int, step: int = 1) -> Generator[int, Any, None]:
    """Generate iterables of numbers between start and end value

    Args:
        start (int): Value from which iterable is to generate
        end (int): Value upto which iterable is to generate
        step (int, optional): Increment value, to increase every subsequent value. Defaults to 1.

    Yields:
        Generator[int, Any, None]: Generator of iterables
    """
    return __range(start, end, step)

a = step(10, 10, 10)