def multiplication_table():
    for outer in range ( 2,5 ):
        print('times table for {0}'.format(outer))
        for inner in range( 1,6 ):
            print('{0] x {1} x {2}'.format(outer,inner,outer*inner))
        print()