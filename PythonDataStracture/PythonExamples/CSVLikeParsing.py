# CSVLikeParsing.py
# Simple CSV parsing without csv module.

line = "name,age,city"
data = [s.strip() for s in line.split(",")]

if __name__ == '__main__':
    print("Columns:", data)