# dice.py

import sys
import random

# Rolls a number of dice for one stat (rolls 3, 4, or 5)
def roll_dice(num_dice):
    # Array to hold each die roll
    roll_results = []
    # The lowest a die can be (in cases of re-rolling 1s and 2s)
    base = 1
    match num_dice:
        case 3:
            base = 3
        case 4:
            base = 2
        case _:
            pass # Figure out Python's "break" statement later
    # Roll the entered quantity
    for _ in range(num_dice):
        roll = random.randint(base, 6)
        roll_results.append(roll)
    roll_results.sort(reverse=True)
    return roll_results[:3]

# Calculate average of a list of integers
def avg(list):
    return sum(list) / len(list)

# Rolls a full set of n stats, dropping the lowest
def roll_group(num_dice):
    # Array to hold the full group
    stats = []
    for _ in range(7):
        roll = roll_dice(num_dice)
        stats.append(sum(roll))
    stats.remove(min(stats))
    print(stats)
    print(avg(stats))

roll_group(int(sys.argv[1]))
