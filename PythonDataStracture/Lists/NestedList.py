# NestedList.py
# A nested list and a small recursive pretty-printer.

nested_list = [1, [2, [3, 4], 5], ["a", ["b", "c"]]]

def flatten(lst):
    out = []
    for item in lst:
        if isinstance(item, list):
            out.extend(flatten(item))
        else:
            out.append(item)
    return out

if __name__ == '__main__':
    print("Nested:", nested_list)
    print("Flattened:", flatten(nested_list))