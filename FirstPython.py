print('Hello Everyone')
about={'name':'Erika', 'loves':'animals', 'age':[42],'profession':'graphic_designer'}
print(about)
if 3>2:
    print('it works!')
name='Sonja'
if name =='Ola':
    print('Hey Ola!')
elif name =='Sonja':
    print('Hey Sonja!')
else:
    print("Hey Friend!")
volume = 57
if volume < 20 :
    print("Its kinda quiet.")
elif 20<= volume < 40:
    print("It's nice for background music.")
elif 40 <= volume < 60:
    print("Perfect, I can hear all the details.")
elif 60 <= volume < 80:
    print("Nice for parties")
elif 80 <= volume < 100:
    print("A bit loud!")
else:
    print("My ears are hurting! :(")
def hi():
    print("Hi there!")
    print("How are you?")
hi()
def hi (name):
    if name == 'Ola':
        print ("Hi Ola!")
    elif name == 'Sonja':
        print("Hi Sonja!")
    else:
        print ("Hi Friend!")
hi('Erika')
hi ('Sophie')
hi ('Ola')

def hi (name):
    print('Hi '+name+'!')
hi("Rachel")

def hi (name):
    print('Hi ' + name + '!')

girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'Erika']
for name in girls:
    hi(name)
    print("Next girl")

for i in range (1,6):
    print (i)
    
