# Author: Eric Stevens 
# A basic text based roulette game using the Martingale algorithm

import random
import os
while(True):
    os.system('cls' if os.name == 'nt' else 'clear')

    print("The Martingale Roulette Experiment")
    print("On a win, you are paid out 2x your bet. ie: $10 bet will payout $20")
    print("On a loss, you quit or double your bet and play again")
    lsm = input("Learn some math? y/n ")
    if(lsm == "y"):
        keepLearning = True
        rnd = 0
        while(keepLearning):
            rnd +=1
            prob = 0.526**rnd
            prob = 1 - prob
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Roulette probability is 0.474")
            print("Probability of winning after "+str(rnd)+" round(s) is: "+str(prob))
            kl = input("Press enter to view next or x to quit ")
            if(kl == "x"):
                keepLearning = False
    else:
        playAgain = True
        totalGain = 0
        while(playAgain):
            bet = input("Enter starting bet: $")
            os.system('cls' if os.name == 'nt' else 'clear')
            bet = int(bet)
            totalBets = bet
            playing = True

            while(playing):
                print("Your bet: $"+str(bet))
                num = random.random()
                print("Roulette Roll: "+str(num))
                if num <= 0.474:
                    payout = 2 * bet
                    print("You win: $"+str(payout))
                    print("You spent $"+str(totalBets)+" on bets")
                    gain = payout - totalBets
                    totalGain += gain
                    print("Your total gain is: $"+str(totalGain))
                    playing = False
                    pA = input("Play again? y/n: ")
                    if(pA == "n"):
                        playAgain = False
                else:
                    print("You lost: $"+str(totalBets))
                    cont = input("Double bet and continue? y/n ")
                    if(cont == "n"):   
                        playing = False
                    else:
                        bet = bet * 2
                        totalBets += bet
                os.system('cls' if os.name == 'nt' else 'clear')


