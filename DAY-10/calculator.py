from art import logo 
from replit import clear

#or there is another version
#import art
#print(art.logo)
def add(num1, num2):
  return num1 + num2
def subtract(num1, num2):
  return num1 - num2
def multiply(num1, num2):
  return num1 * num2
def divide(num1, num2):
  return num1 // num2

#store these functions inside a dictionary 
operations = {"+" : add, 
              "-" : subtract, 
              "*" : multiply, 
              "/" : divide}
def calculator():  
  print (logo)
  number1 = float(input("What is the first number?: "))
  should_end = False
  for i in operations:
      print(i)
  while not should_end:
    operation = input("Pick an operation: ")  
    number2 = float(input("What is the next number?: ")) 
    function = operations[operation]
    result = function(number1, number2)
    print(f"{number1} {operation} {number2} = {result}")
    answer = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation, or type 'end' to finish the calculation: ").lower()
    if answer == "n" :
      clear()
      print("New calculation...")
      calculator()
    elif answer == "y" :
      number1 = result
    elif answer == "end":
      should_end = True
      print("Goodbye...")

calculator()