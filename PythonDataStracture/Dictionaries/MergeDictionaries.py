# MergeDictionaries.py
# Combine two dictionaries using unpacking and update methods.

a = {"x": 1, "y": 2}
b = {"y": 3, "z": 4}

merged = {**a, **b}

if __name__ == '__main__':
    print("Merged dictionary:", merged)