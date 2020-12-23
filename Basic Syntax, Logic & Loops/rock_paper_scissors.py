# Simple cli app using .input() to read user input in python
# Practices conditional logic in python

print("  |||| ROCK ||||")
print(" ||||| PAPER ||||")
print("||||| SCISSORS |||")

p1_choice = input("(enter PLAYER ONE'S choice): ").lower()
if p1_choice == "scissors":
    p1_choice = "scissor"

# while (p1_choice != "rock") or (p1_choice != "paper") or (p1_choice != "scissor"):
#     print("Please enter a valid selection. Check your spelling!")
#     p1_choice = input("(re-enter PLAYER ONE'S choice): ").lower()
#     if p1_choice == "scissors":
#         p1_choice = "scissor"
#     print("P1's Choice: ", p1_choice)
    

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

p2_choice = input("(enter PLAYER TWO'S choice): ").lower()
if p2_choice == "scissors":
    p2_choice = "scissor"

# while not p2_choice == "rock" or not p2_choice == "paper" or not p2_choice == "scissor":
#     print("Please enter a valid selection. Check your spelling!")
#     p2_choice = input("(re-enter PLAYER TWO'S choice): ").lower()
#     if p2_choice == "scissors":
#         p2_choice = "scissor"
#     print("P2's Choice: ", p2_choice)


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
print("P1's Choice: ", p1_choice)
print("P2's Choice: ", p2_choice)

if p1_choice == p2_choice:
    print("It's a tie!")
elif (p1_choice == "rock") and p2_choice == "scissor":
    print("PLAYER 1 WINS!")
elif p1_choice == "scissor" and p2_choice == "paper":
    print("PLAYER 1 WINS!")
elif p1_choice == "paper" and p2_choice == "rock":
    print("PLAYER 1 WINS!")
else:
    print("PLAYER 2 WINS!")