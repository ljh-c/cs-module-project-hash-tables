"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

# q = set(range(1, 10))
# q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

def sum_f(a, b):
    return f(a) + f(b)

def diff_f(c, d):
    return f(c) - f(d)

sums = {}
diffs = {}

for num_c in q:
    for num_d in q: 
        # OK to store result as key because c - d != d - c
        diffs[diff_f(num_c, num_d)] = (num_c, num_d)

for num_a in q:
    for num_b in q:
        # Store args as key because different args can have same result
        if sum_f(num_a, num_b) in diffs:
            sums[(num_a, num_b)] = sum_f(num_a, num_b)

# print(diffs)
# print(sums)

for k, v in sums.items():
    match = diffs[v] # tuple of args

    print(f'f({k[0]}) + f({k[1]}) = f({match[0]}) - f({match[1]})    {f(k[0])} + {f(k[1])} = {f(match[0])} - {f(match[1])}')

