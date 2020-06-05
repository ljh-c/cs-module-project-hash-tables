# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

"""
Only one letter to letter
Get the frequency by percentage of each letter in the text
Sort by frequency
Map the letter to its closest partner using the table
"""

from collections import OrderedDict

with open('ciphertext.txt') as file:
    words = file.read()

freq = {}

for char in words:
    if char.isalpha(): 
        if char not in freq:
            freq[char] = 0
        
        freq[char] += 1

freq_arr = sorted(freq.items(), key=lambda w: -w[1])

english_freq = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U',
'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']

rosetta = dict(zip([k for k, v in freq_arr], english_freq))

print(rosetta)

with open('decoded.txt', 'w') as cracked:
    for char in words:
        if char.isalpha():
            cracked.write(rosetta[char])
        else:
            cracked.write(char)