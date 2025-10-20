# ContextManagerDemo.py
# Use contextlib to create a simple context manager.

from contextlib import contextmanager

@contextmanager
def simple_cm():
    print("enter")
    try:
        yield
    finally:
        print("exit")

if __name__ == '__main__':
    with simple_cm():
        print("inside")