
# This was my first try and was able to compare input


print ("This machine will tell you whos the winner:")
input ("Are you ready? press enter:")
hand1 = input ('Enter first hand:  ')
hand2 = input ('Enter second hand:  ')

print ('Now lets find out which hand wins, is it' ' '+ hand1 + ' ''or' ' '+hand2)
input ('loading...press enter to find out who wins:')

values = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "T":10, "J":11, "Q":12, "K":13, "A":14}
values = {"c":1, "d":2, "h":3, "s":4}
 

class high_low():
    def __init__(self):
        if hand1 < hand2:
            print ('hand2 wins')
        else: 
            print ('hand1 wins')
        return    

high_low()