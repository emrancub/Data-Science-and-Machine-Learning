#UniquePreserveOrder.py
#Remove duplicates while preserving order using dict.fromkeys....

def unique_preserve(seq):
    return list(dict.fromkeys(seq))

if __name__ == '__main__':
    print(unique_preserve([3,1,4,1,5,9,3]))