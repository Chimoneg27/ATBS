# This program says hello and asks for my name
# The print() function displays the string value inside its parentheses on the screen.
print('Hello, world!');
print('What is your name?'); # ask for their name

myName = input(); # The input() function waits for the user to type some text on the keyboard and press enter

print('It is good to meet you, ' + myName);
print('The length of your name is:')
print(len(myName))

print('What is your age?') # ask for their age
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year')