data = {
  "name": "Maryus",
  "age": 29,
}

def greeting(name, age):
    return 'Hi, My name is {} and Im {} years old'.format(name, age)

print(greeting(**data))

def foo(**kwargs):
  for key, value in kwargs.items():
    print("{}:{}".format(key, value))


foo(name = "Maryus", age = 29)

def add(*numbers):
    total = 0
    for number in numbers:
        total = total + number
    return total

total = add(1,2,3,4)

print('total is: ', total)