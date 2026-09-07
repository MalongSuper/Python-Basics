# Python Generators
def factors(n):
    for val in range(1, n + 1):
        if n % val == 0:
            yield val


print(factors(20))

for factor in factors(20):
    print(factor, end=" ")


# Generators Remember Their State
def yield_multiple_statements():
    yield "This is the first statement"
    yield "This is the second statement"
    yield "This is the third statement"
    yield "This is the last statement. Don't call next again!"


example = yield_multiple_statements()
print(next(example))
print(next(example))
print(next(example))
print(next(example))


# Custom Range Generator
def custom_range(start, stop, step=1):
    current = start

    while current < stop:
        yield current
        current += step


for num in custom_range(2, 10, 2):
    print(num, end=" ")


# Vowel Filter
def vowel_filter(text):
    vowels = "aeiou"

    for char in text:
        if char.lower() in vowels:
            yield char


for vowel in vowel_filter("Hello, World!"):
    print(vowel, end=" ")


# Fibonacci Generator
def fibonacci(n):
    a, b = 0, 1

    for _ in range(n):
        yield a
        a, b = b, a + b


for num in fibonacci(8):
    print(num, end=" ")


# Infinite Generator
def infinite_counter(start=1):
    current = start
    while True:
        yield current
        current += 1


for num in infinite_counter():
    if num > 5:
        break
    print(num, end=" ")

# Manual Iterator Handling
numbers = [10, 20, 30]
iterator = iter(numbers)

while True:
    try:
        value = next(iterator)
        print(value, end=" ")
    except StopIteration:
        break


# Generator Pipelines
def number_producer(iterable):
    for item in iterable:
        yield item


def squarer(iterable):
    for num in iterable:
        yield num ** 2


numbers = [1, 2, 3, 4, 5]
pipeline = squarer(number_producer(numbers))
for value in pipeline:
    print(value, end=" ")


# Flatten Nested Lists
def flatten(nested):
    for item in nested:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item


nested = [1, [2, [3, 4], 5], [6, 7], 8]
for value in flatten(nested):
    print(value, end=" ")


# Batch Processing
def batch(iterable, batch_size):
    items = list(iterable)
    for i in range(0, len(items), batch_size):
        yield items[i:i + batch_size]


for chunk in batch(range(1, 11), 3):
    print(chunk)


# Prime Number Generator
def prime_sieve(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(limit ** 0.5) + 1):
        if is_prime[i]:
            is_prime[i * i::i] = [False] * len(is_prime[i * i::i])
    for i in range(2, limit + 1):
        if is_prime[i]:
            yield i


for prime in prime_sieve(30):
    print(prime, end=" ")


# Running Average
def running_average(iterable):
    total = 0
    count = 0
    for value in iterable:
        total += value
        count += 1
        yield total / count


numbers = [10, 20, 30, 40, 50]
for avg in running_average(numbers):
    print(avg, end=" ")


# Sliding Window
def sliding_window(sequence, n):
    items = list(sequence)
    for i in range(len(items) - n + 1):
        yield tuple(items[i:i + n])


sequence = [1, 2, 3, 4, 5]
for window in sliding_window(sequence, 3):
    print(window, end=" ")


# Unique Values Generator
def unique(iterable):
    seen = set()
    for item in iterable:
        if item not in seen:
            seen.add(item)
            yield item


items = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
for value in unique(items):
    print(value, end=" ")
