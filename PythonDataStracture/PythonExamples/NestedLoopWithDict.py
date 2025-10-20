# NestedLoopWithDict.py
# Build a frequency dictionary of characters per word.

words = ["apple", "banana", "cherry"]

def freq_per_word(words):
    result = {}
    for w in words:
        d = {}
        for ch in w:
            d[ch] = d.get(ch, 0) + 1
        result[w] = d
    return result

if __name__ == '__main__':
    print("Frequencies:", freq_per_word(words))