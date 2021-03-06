from gingerit.gingerit import GingerIt

# Allow input text from user
userInput = input("Please enter your text with spelling errors:   ")

# Creating the ginger object
gingerObj = GingerIt()

# Passing the text as a parameter usig the parse function

result = gingerObj.parse(userInput)


# Print the corrected text
print("Original Text: ", result['text'])
print()

print("Corrected Text: ", result['result'])
