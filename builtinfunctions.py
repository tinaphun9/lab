print("challenege start")

answer = input("How many zeros are in a million? ")

zeros = int(answer)   
print("You entered:", zeros)
print("The type of your answer is:", type(zeros))

correct = 6
difference = abs(correct - zeros)

if zeros == correct:
    print("good job, if you could have a million of something, what would it be?")
else:
    print("Not correct.")
    print("You were off by", difference)

# Count digits using len()
million = 1000000
million_text = str(million)
print("1,000,000 has", len(million_text), "total digits.")

# Let user choose something to have a million of
print("What would you like a million of?")
print("1 - fur | 2 - rocks | 3 - puzzle pieces")

choice = input("Enter 1, 2, 3 ")

if choice == "1":
    print("You have fur")
else:
    if choice == "2":
        print("its just sand")
    else:
        if choice == "3":
            print("all the puzzles pieces arent from the same set")
        else:
            print("try again")

numbers = [10, 500, 1000000, 25, 300]
print("Smallest number in list:", min(numbers))
print("Largest number in list:", max(numbers))
math_problem = input("\nType a math problem (example: 5+5): ")
result = eval(math_problem)
print("Your answer is:", result)
print(dir(zeros))
