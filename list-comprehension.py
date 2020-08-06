data = {
  "name": "Maryus",
  "age": 29,
}

def greeting(name, age):
    return 'Hi, My name is {} and Im {} years old'.format(name, age)

def foo(**kwargs):
  for key, value in kwargs.items():
    print("{}:{}".format(key, value))

def add(*numbers):
    total = 0
    for number in numbers:
        total = total + number
    return total

total = add(1,2,3,4)


def solve(s):
    indexes = [i for i, c in enumerate(s) if c == " "]
    result = "".join([c for c in s if c!=" "])[::-1]

    for index in indexes:
      result = result[:index] + " " + result[index:]
      
    return result

print(solve("our code"))