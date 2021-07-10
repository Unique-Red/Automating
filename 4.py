from typing import Match


while True:
    name = input('What is your name?: ')
    # name = input()
    if len(name)>5:
        break
    else:
        print('input your full name')

while True:
    try:
        age = int(input('how old are you?: '))
        age_limit = age
        if age_limit >= 18:
            break
        else:
            print('you must be at least 18 years old')
            quit()
    except ValueError:
        print('age must be in number')

while True:
    username = input('choose a username: ')
    if len(username) >= 5:
        break
    else:
        print('username must have more than five characters')

while True:
    password =input('choose a password: ')
    if password == "password":
        print('password cannot be PASSWORD')
        quit()
    else: 
        pass
    if len(password)>= 8:
        break
    else:
        print('password must be eight or more characters')

confirm_password = input('confirm your password: ')
if confirm_password == password:
    print('hi {} . you are {} years old'. format(name,age))
    print('profile has been created')
else:
    print('incorrect password, this password can\'t be assigned')
    print('profile cannot be created')

while True:
    print('Who are you?')
    na_me = input()
    if na_me == username:
        print('Hello ' + username + ' What is the password?.')
    else:
        pass

    pass_word = input()
    if pass_word == password:
        break
print('Access granted.')

print('{program finished}')
print('{program finished}')
print('')
print('')
print('')