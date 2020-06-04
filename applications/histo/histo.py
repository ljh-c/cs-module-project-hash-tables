file = input('Enter name of file: ')

with open(f'{file}.txt') as f:
    words = f.read()

freq = {}

arr = words.split()

table = str.maketrans(dict.fromkeys('":;,.-+=/\\|[]{}()*^&'))

for w in [word.lower().translate(table) for word in arr]:
    if w not in freq:
        freq[w] = 0

    freq[w] += 1

freq_arr = list(freq.items())

freq_arr.sort(key=lambda w: (-w[1], w[0]))

# Get longest word
longest_word, v = max(freq_arr, key=lambda w: len(w[0]))
# print(len(longest_word))

# print(freq_arr)

sep = '#'

for k, v in freq_arr:
    print(f'{k:{len(longest_word) + 1}} {"#" * v}')