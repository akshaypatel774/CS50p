# Get input
camel = input("camelCase: ")
snake = ""
# Check upper and replace
for letter in camel:
    if letter.isupper():
        snake += "_" + letter.lower()
    else:
        snake += letter

print(snake)