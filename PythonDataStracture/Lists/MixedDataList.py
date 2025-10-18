# MixedDataList.py
# A list that contains mixed data types.

mixed_list = [42, "hello", 3.14, True, None]

def describe_list(lst):
    return [(type(x).__name__, x) for x in lst]

if __name__ == '__main__':
    print("Mixed list description:", describe_list(mixed_list))