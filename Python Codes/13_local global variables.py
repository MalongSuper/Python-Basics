# Local and Global Variables
name = "Iris"
age = 18
height = 1.65

print(name)
print(age)
print(height)


# Local Variables
def greet():
    message = "Hello World"
    print(message)


greet()


def greet():
    message = "Hello World"
    return message


message = greet()
print(message)


def student1():
    score = 90
    print(score)


def student2():
    score = 75
    print(score)


student1()
student2()


# Global Variables
message = "Welcome to Python"


def greet():
    print(message)


greet()


message = "Global Variable"


def display():
    print(message)


display()
print(message)

# Change the variable
message = "This is a variable"
display()
print(message)


count = 10


def update():
    global count
    count = count + 1
    print(count)


update()
print(count)


# Global vs Local with the Same Name
a = "I am Global Iris"


def print_name():
    a = "I am Local Iris"
    print(a)


print_name()
print(a)


# Modifying Global Variables Inside a Function
a = 1


def modify1():
    print("modify1:", a)


def modify2():
    a = 2
    print("modify2:", a)


def modify3():
    global a
    a = 4
    print("modify3:", a)


print("global:", a)
modify1()
print("global:", a)
modify2()
print("global:", a)
modify3()
print("global:", a)
