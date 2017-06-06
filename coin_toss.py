
import random

def toss(reps):
    print "Starting the program, hold onto your pants!"
    counterhead = 0
    countertails = 0
    for x in range (0, reps):
        score = random.randint(0, 1)
        if round(score) == 1:
            counterhead = counterhead + 1
            print "Throwing a coin... It's a head! ... Got", counterhead, "head(s) so far and", countertails, "tail(s) so far"
        elif round(score) == 0:
            countertails = countertails + 1
            print "Throwing a coin... It's a tails! ...Got", counterhead, "head(s) so far and", countertails, "tail(s) so far"
    print "Ending the program, thank you!"
toss(200)
