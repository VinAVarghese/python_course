# Simple cli app using .input() to read user input in python
# Practices conditional logic in python with randint method for AI player
    #random needs to be imported to use ".randint()"
import random

print("  |||| ROCK ||||")
print(" ||||| PAPER ||||")
print("||||| SCISSORS |||")

p_choice = input("(enter PLAYER'S choice): ").lower()
if p_choice == "scissors":
    p_choice = "scissor"

# while (p_choice != "rock") or (p_choice != "paper") or (p_choice != "scissor"):
#     print("Please enter a valid selection. Check your spelling!")
#     p_choice = input("(re-enter PLAYER ONE'S choice): ").lower()
#     if p_choice == "scissors":
#         p_choice = "scissor"
#     print("P's Choice: ", p_choice)
    

print("************ NO CHEATING **************")
print("************ NO CHEATING **************")
print("************ NO CHEATING **************")
print("************ NO CHEATING **************")
print("************ NO CHEATING **************")
print("************ NO CHEATING **************")
print("************ NO CHEATING **************")
print("************ NO CHEATING **************")
print("************ NO CHEATING **************")
print("************ NO CHEATING **************")
print("************ NO CHEATING **************")
print("************ NO CHEATING **************")
print("************ NO CHEATING **************")
print("************ NO CHEATING **************")
print("************ NO CHEATING **************")

AI_choice = random.randint(1,3)

if AI_choice == 1:
    AI_choice = "rock"
elif AI_choice == 2:
    AI_choice = "scissor"
elif AI_choice == 3:
    AI_choice = "paper"


print("************ and ... **************")
print("************ and ... **************")
print("************ and ... **************")
print("************ and ... **************")
print("************ and ... **************")
print("************ and ... **************")
print("************ and ... **************")
print("************ and ... **************")
print("************ and ... **************")
print("************ and ... **************")
print("************ and ... **************")
print("************ and ... **************")
print("************ and ... **************")
print("************ and ... **************")
print("************ and ... **************")

print("SHOOT!")

print("PLAYER'S CHOICE: ", p_choice)
print("AI'S CHOICE: ", AI_choice)

if p_choice == AI_choice:
    print("It's a tie!")
elif (p_choice == "rock") and AI_choice == "scissor":
    print("PLAYER  WINS!")
elif p_choice == "scissor" and AI_choice == "paper":
    print("PLAYER  WINS!")
elif p_choice == "paper" and AI_choice == "rock":
    print("PLAYER  WINS!")
else:
    print("AI WINS!")