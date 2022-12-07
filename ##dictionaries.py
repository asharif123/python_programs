##dictionaries
#each key should be unique
customer = {
    "name": "Awad Sharif",
    "age": 32,
    "is_verified": True
}
print(customer["name"])
customer["name"] = "Jason"
customer["birthdate"] = "Jan 23, 1990"
print(customer)

##ask for phone number, type in digits and translate to words
digits_mapping = {"1":'One',"2":"Two","3":"Three","4":"Four","5":"Five","6":"Six","7":"Seven","8":"Eight","9":"Nine","0":"Zero"}

# number = input('')
# output = ""

# for digit in number:
#     print(digit)
#     output += digits_mapping[digit] + " "
# print(output)

##emoji converter
message = input("")
#finds space and uses as boundary to separate into multiple words
words = message.split(' ')
print(words)
emojis = {
    ":)": "😃",
    ":(": "😔"
}
output = ''
for word in words:
    ##if word key exists in dict, print its corr value. ELSE just print the word
    output += emojis.get(word, word) + " "
print(output)
