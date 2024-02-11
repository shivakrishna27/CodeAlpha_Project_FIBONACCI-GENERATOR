
def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


def fibonacci_iterative(n):
    fib_sequence = [0, 1]
    for i in range(2, n+1):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[n]


def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


n = 10
print("Recursive Fibonacci sequence:")
for i in range(n):
    print(fibonacci_recursive(i), end=" ")
print()


print("Iterative Fibonacci sequence:")
for i in range(n):
    print(fibonacci_iterative(i), end=" ")
print()

print("Generator Fibonacci sequence:")
fib_gen = fibonacci_generator()
for _ in range(n):
    print(next(fib_gen), end=" ")
