name = input('')
if (len(name) < 3):
    print("Name must have at least 3 characters!")
elif(len(name) > 50):
    print("Name can have up to 50 characters!")
else:
    print("Name looks good!")