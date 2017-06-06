
import random

def grade(reps):
    print "Scores and Grades"
    for x in range(0, reps):
        score = random.randint(60, 101)
        if score >= 60 and score <= 69:
            print "Score: ", score,"; Your grade is D, try harder!"
        elif score >= 70 and score <= 79:
            print "Score: ", score, "; Your grade is C, pretty average."
        elif score >= 80 and score <= 89:
            print "Score: ", score, "; Your grade is B, well done!"
        elif score >= 90 and score <= 100:
            print "Score: ", score, "; Your grade is A, great job!"
        else:
            print "You failed"
    print "End of the program.  Bye!"

grade(1)