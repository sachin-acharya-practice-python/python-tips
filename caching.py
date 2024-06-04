from functools import lru_cache, cache


# Function to calculate Fibonacci series
@lru_cache # Can use cache as well. Read docs to know difference between these two.
def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


for i in range(0, 41):
    print(f"{i}: {fibonacci(i)}")
