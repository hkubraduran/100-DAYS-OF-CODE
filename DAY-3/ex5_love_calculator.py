# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
total_true = 0
total_love = 0
combine_name = name1 + " " + name2
uppercase_name = combine_name.upper()

total_true += uppercase_name.count("T")
total_true += uppercase_name.count("R")
total_true += uppercase_name.count("U")
total_true += uppercase_name.count("E")

total_love += uppercase_name.count("L")
total_love += uppercase_name.count("O")
total_love += uppercase_name.count("V")
total_love += uppercase_name.count("E")

total_score = str(total_true) + str(total_love)
love_score = int(total_score)
if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score < 50 and  love_score > 40:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")