import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
markov = {}

arr = words.split()

markov[arr[0]] = []

curr = arr[0]

for word in arr[1:]:
    if curr not in markov:
        markov[curr] = []

    markov[curr].append(word)

    curr = word

# print(random.choice(list(markov.keys())))

# TODO: construct 5 random sentences
for _ in range(5):
    start = " "

    while not (start[0].isupper() or (start[0] == "\"" and start[:2].isupper())):
        start = random.choice(list(markov.keys()))

    print(start, end=" ", flush=True)

    next_word = random.choice(markov[start])

    print(next_word, end=" ", flush=True)

    while not (next_word[-1] == "." or next_word[-1] == "?" or next_word[-1] == "!" or next_word[-2:] == ".\"" or next_word[-2:] == "?\"" or next_word[-2:] == "!\""):
        next_word = random.choice(markov[next_word])
        
        print(next_word, end=" ", flush=True)
    
    print("\n")

input("Press enter to close program.")