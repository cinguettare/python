import easygui as g
import sys
import random

def choice():
    msg = "Do you want to start the game again?"
    title = "please choose"
    
    if g.ccbox(msg, title):
        pass
    else:
        sys.exit(0)
        


def game():
    
    times = 3
    num = random.randint(1, 10)
    
    while 1:

        times = times - 1
    
        msg = 'Try to guess what the number is (1~10): '
        title = 'number game'
        E_num = g.integerbox(msg, title, lowerbound=1, upperbound=10)

        if E_num == num:
            g.msgbox("Yeah, you're right!")
            choice()
        else:
            if E_num > num:
                g.msgbox("Oh, it's big!")

            else:
                g.msgbox("No, it's small!")

            if times > 0:
                g.msgbox("Come again!")
                
            else:
                g.msgbox("Opportunity to run out!")
                choice()


if __name__ == "__main__":
    game()
