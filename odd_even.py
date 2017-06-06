def odd_even(min, max):
    for count in range(0, 2001):
        if count % 2 == 0:
            print count, "is an even number"
        else:
            print count, "is an odd number"
print odd_even(0, 2001)
