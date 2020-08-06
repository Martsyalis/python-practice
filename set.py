def get_count(input_str):
    return sum(1 for c in input_str if c in 'aeou')

print(get_count('aeousssssss'))


def friend(x):
    return sum([1 for f in x if f in 'ad'])

print(friend('abcd'))