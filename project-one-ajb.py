'''
Script for finding out more about AJB.
'''
answerPos = "It's the Batmobile!"
answerNeg = "You're missing out."
print('''Hi, I'm AJB, and I want us to be friends.
Want to know what my favorite car is?''')
response = input()
response = response.lower()
print("I thought you'd say " + response + '!')
if response == 'yes' or 'sure' or 'why not':
    print(answerPos), input('BFFs, forever!')
else:
    print(answerNeg), input('Good luck being miserable though.')