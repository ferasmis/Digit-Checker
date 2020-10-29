## Author: Feras
## Description: Check if user input is a digit or not

inputStr = input("Enter a value:\n")
while inputStr.isnumeric() == False:
    print("Invalid input\n")
    inputStr = input("Enter a value:\n")
print("You entered " + inputStr)
