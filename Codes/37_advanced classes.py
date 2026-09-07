# Advanced Examples With Classes

# Even Iterator
class EvenIterator:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.limit:
            raise StopIteration

        value = self.current
        self.current += 2

        return value


for num in EvenIterator(10):
    print(num, end=" ")


# Reverse String Iterator
class ReverseStringIterator:
    def __init__(self, text):
        self.text = text
        self.index = len(text) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration

        char = self.text[self.index]
        self.index -= 1

        return char


for char in ReverseStringIterator("hello"):
    print(char, end=" ")


# Float Step Iterator
class FloatStepIterator:
    def __init__(self, start, stop, step):
        self.current = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.stop:
            raise StopIteration

        value = self.current
        self.current = round(self.current + self.step, 10)

        return value


for num in FloatStepIterator(0.0, 1.0, 0.25):
    print(num, end=" ")
