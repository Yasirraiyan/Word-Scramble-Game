import math
import time

s = 'Pokemone'
correct = 'one'
duration = 10
chance = 5
score = 0

guessword = input("Enter your guess:")
p = list(s)
print(p)

q = len(s)
print(q)

permutation = (math.factorial(q)) / math.factorial(2)
print(permutation)

start = time.time()
end = time.time()
need = end - start
print(need)

while need < duration:
    need -= 2
    chance -= 1  # Changed to decrement by 1
    score += 10
    print(f"Left time: {need}")
    print(f"Left chance: {chance}")
    print(f"Score: {score}")

    if chance == 0:
        print("Game Over!")
        print(f"Final score is: {score}")
        break  # Added a break statement to exit the loop when the game is over

    if guessword == correct:
        print("Win")
        score += 10
        print(f"Score: {score}")
        break  # Added a break statement to exit the loop when the user wins
    else:
        print("Loss!")  # This else statement is outside the if-else block for guessword comparison
