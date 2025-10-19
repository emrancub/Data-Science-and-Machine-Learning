# ImmutableNature.py
# Demonstrate that tuples are immutable.

values = (1, 2, 3)

try:
    values[0] = 99
except TypeError as e:
    print("Error:", e)

print("Tuples cannot be changed after creation.")