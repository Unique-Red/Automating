def spam():
    global eggs
    eggs = 'spam' #global scope

def bacon():
    eggs = 'bacon' #local scope

def ham():
    print(eggs) #global scope

eggs = 42 #global scope
spam()
print(eggs)