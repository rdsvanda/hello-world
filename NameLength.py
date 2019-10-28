name_entered = input('What is your name?')

print(len(name_entered))



if len(name_entered) < 3:
    print('Name is too short, must be at least 3 characters.')

elif len(name_entered) > 50:
    print('Name is too long, must be less than 50 characters.')

else:
    print('Name Accepted, thank you.')

