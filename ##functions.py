##functions
def greet_user(first_name, last_name):
     return "Hello there %s %s!" %(first_name, last_name)
print(greet_user("Awad","Sharif"))

#keyword arguments
##if combined with positional, use keyword arguments after positional arguments
print(greet_user(last_name="Sharif", first_name="Awad"))

def square(number):
    return number * number
result = square(3)
print(result)

##emoji converter function
def emoji_converter(sentence):
    sentence = sentence.split(' ')
    emoji_mapping = {
        ":)": "😃",
        ":(": "😔"
    }
    output = ''
    for word in sentence:
        output += emoji_mapping.get(word,word) + " "
    return output

print(emoji_converter("Good morning :)"))
print(emoji_converter("Having a bad day :("))
