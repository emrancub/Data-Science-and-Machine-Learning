# TupleAndListInterplay.py
# Convert tuples to lists, modify, and convert back.

coords_tuple = (1, 2, 3)
coords_list = list(coords_tuple)
coords_list.append(4)
coords_tuple2 = tuple(coords_list)

if __name__ == '__main__':
    print("Original tuple:", coords_tuple)
    print("Modified tuple:", coords_tuple2)