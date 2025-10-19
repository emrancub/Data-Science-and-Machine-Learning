#MixedTuple.py
# A tuple with mixed data types.

mixed = (1, "hello", 3.15, False, None, "emran")

if __name__ == '__main__':
    for item in mixed:
        print(f"{item!r} is of type {type(item).__name__}")