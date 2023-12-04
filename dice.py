# dice.py

import random

def roll_dice(num_dice):
    roll_results = []
    for _ in range(num_dice):
        roll = random.randint(2, 6)
        roll_results.append(roll)
    return roll_results

def avg(list):
    return sum(list) / len(list)

def roll_group(num_groups):
    stats = []
    for _ in range(num_groups):
        roll = roll_dice(4)
        roll.remove(min(roll))
        stats.append(sum(roll))
    stats.remove(min(stats))
    print(stats)
    print(avg(stats))

roll_group(7)
