print ("Let's practice everything!")
print("You need to \' escape it\'s then do newlines \n and tabs \t")

print("\tThe lovely world \n needs the love \n of attention!")
print("---------")

five = 10 - 2 + 3 - 6
print("This should be %s" %(five))

def secret_formula(started):
    jelly_beans = started * 1000
    jars = jelly_beans / 500
    crates = jars / 100
    return jelly_beans, jars, crates

print(secret_formula(2000))

#split 
def break_words(stuff):
    words = stuff.split(' ')
    return words

##sorted
def sort_words(words):
    return sorted(words)

#print first word
def print_first_word(words):

    word = words.pop(0)
    print (word)

def print_last_word(words):
    print(words.pop(-1))

def sort_sentence(sentence):
    sorted = sort_words(sentence)
    break_word = break_words(sorted)
    return break_word

def print_first_and_last(sentence):
    words = break_words(sentence)
    return words[0], words[-1]
    
def print_first_last_sorted(sentence):
    sorted_sentence = sorted(sentence)
    return print_first_word(sorted_sentence), print_last_word(sorted_sentence)