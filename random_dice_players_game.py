import random

score1 = 0
score2 = 0

print("Player 1 Starts")
for i in range(1, 4):
    roll1 = random.randint(1, 6)
    print(f"Player 1 Rolled Dice: {roll1}")
    score1 += roll1

print("\nPlayer 2 Starts")
for j in range(1, 4):
    roll2 = random.randint(1, 6)
    print(f"Player 2 Rolled Dice: {roll2}")
    score2 += roll2

print("\n--- Final Result ---")
print(f"Player 1 total score: {score1}")
print(f"Player 2 total score: {score2}")

if score1 > score2:
    print("First player wins!")
elif score1 == score2:
    print("The two players drew")
else:
    print("Second player wins!")
