'''
I had trouble trying to get the while loop to work. 
I’m aware that both conditions need to be true for 
it to carry on to the next function, but I haven’t 
worked out the solution yet. 
'''

value = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "T":10, "J":11, "Q":12, "K":13, "A":14}
suit = {"C":1, "D":2, "H":3, "S":4}


class PokerHand:
    
    
    def check(self):
       
        global hand1 
        hand1 = input ('Enter first hand:  ')
        
        while hand1 not in value and suit:
            print ('You have entered a wrong card in hand1')
            hand1 = input ('Enter first hand:  ')
         

    def check2(self):
        
        global hand2 
        hand2 = input ('Enter second hand:  ')
       
        while hand2 not in value and suit:
            print ('You have entered a wrong card in hand2')
            hand2 = input ('Enter second hand:  ')
         

                
f = PokerHand()
f.check()
f.check2()









  
   















