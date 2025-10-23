# ZipAndUnzip.py
# Use zip to combine lists and unzip back.

names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

zipped = list(zip(names, scores))
names2, scores2 = zip(*zipped)

if __name__ == '__main__':
    print("Zipped:", zipped)
    print("Unzipped names:", names2)
    print("Unzipped scores:", scores2)