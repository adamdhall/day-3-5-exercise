# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
lowercase_1 = name1.lower()
lowercase_2 = name2.lower()

x=lowercase_1.count("t") + lowercase_2.count("t") +lowercase_1.count("r") + lowercase_2.count("r") + lowercase_1.count("u") + lowercase_2.count("u") + lowercase_1.count("e") + lowercase_2.count("e")

y=lowercase_1.count("l")+ lowercase_2.count("l") + lowercase_1.count("o") + lowercase_2.count("o") + lowercase_1.count("v") + lowercase_2.count("v") + lowercase_1.count("e") + lowercase_2.count("e")

score = int(str(x) + str(y))
if score < 10 or score > 90:
  print(f"your score is {score}. You go together like coke and mentos.")
elif score > 40 and score < 50:
  print(f"your score is {score}. You go alright together.")
else:
  print(f"Your score is {score}.")