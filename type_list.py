x=[3, "q", "grump", 44, "hork"]
for element in x:
    if type(x) == int:
        for int in x:
            sum = sum + int
        print sum
        #then add int to previous int
    else:
        for str in x:
            s=","
            cmbn += str
            print s.join(cmbn)
            #then add all the strings into a new list and reprint
