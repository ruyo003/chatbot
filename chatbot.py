
print('''welcome to HeyPal, your all in one app that makes your freshman journey
easier to navigate!
please enter your credentials below to get started
''')

name = input('please enter your name: ').lower()
age = int(input('please enter your age: '))
colour = input('please enter your favourite colour: ').lower()

print(f'''
hello {name}! I can see that your favourite colour is {colour}.
Based on your choice, below are a few suggestion on clubs you could join.
''')

if colour == 'green':
    print('i see your favourite colour is green, check out the following club options you can join: ')
    print('''
1. our nature/agriculture club.
2. our green themed hockey club.
3. our green themed book club.
    ''')
elif colour == 'red':
    print('i see your favourite colour is green, check out the following club options you can join: ')
    print('''
 1. our red themed law club.
2. our boxing club.
3. our red colour themed drama club
''')
elif colour == 'blue':
    print('i see your favourite colour is blue, check out the following club options you can join: ')
    print('''
1. our swimming club
2. our deep sea exploration club
3. our blue themed art club
''')
elif colour == 'yellow':
    print('i see your favourite colour is yellow, check out the following club options you can join: ')
    print('''
1. our dance club
2. our math club
3. our hiking club
4. our warewolf club
''')
else:
    print("i'm not sure if that was a colour you have entered, please try again. ")

if age <= 22:
    print('here are some events you might fancy:')
    print('''
1. hiking every wednesday
2. movie night every friday
3. video games competition saturday afternoon
4. youth service volunteer
''')

else:
    print('here are a few suggestions that might interest you: ')
    print('''
 1. study groups
 2. cancer research club 
 3. community service volunteer
''')

# frequently asked questions

question = input("do you have any additional questions: ")

if question == 'how is learning in this institution':
    print('this institution is among the top 5 franked in our country!')

