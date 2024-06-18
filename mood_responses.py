import os

def loving():
    print("I'm so glad you're feeling loving. Love always wins!")

def happy():
    print("I'm glad that you're glad! Rock on and carry on.")

def fearful():
    print("You're not alone in this. We'll get through it together")

def surprised():
    print("What a world we live in, amirite?")

def sad():
    print("I'm sorry you feel down. This too shall pass.")

def angry():
        print("Deep breaths. This too shall pass.")

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
