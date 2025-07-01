# Task 5: For Loops

import random

# 1. Simulate rolling a 6-sided die
rolls = [random.randint(1, 6) for _ in range(20)]
print("Dice Rolls:", rolls)

six_count = rolls.count(6)
one_count = rolls.count(1)
consecutive_sixes = sum(1 for i in range(len(rolls)-1) if rolls[i] == rolls[i+1] == 6)

print("Number of 6s rolled:", six_count)
print("Number of 1s rolled:", one_count)
print("Number of consecutive 6s rolled:", consecutive_sixes)

# 2. Jumping Jack Routine
completed = 0
while completed < 100:
    print(f"\nDo 10 jumping jacks. Completed so far: {completed}")
    tired = input("Are you tired? (y/n): ").lower()
    if tired in ["y", "yes"]:
        skip = input("Do you want to skip remaining sets? (y/n): ").lower()
        if skip in ["y", "yes"]:
            print(f"You completed a total of {completed} jumping jacks.")
            break
    completed += 10
else:
    print("🎉 Congratulations! You completed the workout!")
