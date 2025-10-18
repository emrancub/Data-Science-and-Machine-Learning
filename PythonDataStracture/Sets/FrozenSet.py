# FrozenSet.py
# Demonstarate immutability of frozenset

frozen = frozenset([1, 2, 3])

if __name__ == '__main__':
    print("Frozen set:", frozen)
    try:
        frozen.add(4)
    except AttributeError as e:
        print("Error:", e)