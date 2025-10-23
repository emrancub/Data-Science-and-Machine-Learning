#WeightedChoiceDemo.py
#Simple weighted random choice

import random
def weighted_choice(items, weights):
    total = sum(weights)
    r = random.uniform(0, total)
    upto = 0
    for item, w in zip(items, weights):
        if upto + w >= r:
            return item
        upto += w

if __name__ == '__main__':
    print(weighted_choice(['a','b','c'], [1,2,3]))