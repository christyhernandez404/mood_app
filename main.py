import mood_responses as m
import time

mood = []


def main(mood):
    while True:
        mood = input('''
Welcome to the mood app! We're here for you! 
1 - Loving
2 - Happy
3 - Fearful
4 - Surprised
5 - Sad
6 - Angry
7 - Quit Application

Select the choice below that most closely describes your mood:''')
        if mood == '1':
            m.loving()
            time.sleep(5)
            m.clear()
        elif mood == '2':
            m.happy()
            time.sleep(5)
        elif mood == '3':
            m.fearful()
            time.sleep(5)
            m.clear()
        elif mood == '4':
            m.surprised()
            time.sleep(5)
            m.clear()
        elif mood == '5':
            m.sad()
            time.sleep(5)
            m.clear()
        elif mood == '6':
            m.angry()
            time.sleep(5)
            m.clear()
        elif mood == '7':
            print("See ya next time!")
            time.sleep(3)
            break
        else:
            print("invalid operation")


main(mood)
