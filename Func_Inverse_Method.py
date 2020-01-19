# from sympy import symbols, solve_linear_system, Matrix


def inverse_method():
    # Linear Algebra Matrix With Maximum 6x6 Dimensions Solved By Inverse Matrix Method
    print('')
    print("Linear Algebra Matrix With Maximum 6x6 Dimensions Solved By Inverse Matrix Method")
    print('')
    print("This is an algorithm to solve Linear Equation Systems by using Inverse Matrix Method.")
    print("The coefficients of 'x', 'y', 'z', etc. and the result must be written with a space('') in between.")
    print("The coefficients and the result must be integers, not fractions or irrationals.")
    print('')
    print("Example Input = -1 0 5 9")
    print("Meaning of Example Input = -1x + 5z = 9")
    print('')

    # Converting Equations To Lists and Conversion Of All Elements To Floats
    dimensions = str(input('Enter Dimensions Of The Matrix: '))
    print('')

    row_count = dimensions
    column_count = dimensions

    while int(row_count) > 6 or int(column_count) > 6:
        print('Max Dimensions Are 6x6!')
        print('')
        dimensions = str(input('Enter Dimensions Of The Matrix: '))
        row_count = dimensions
        column_count = dimensions

    row_count = int(dimensions)
    column_count = int(dimensions)

    containers = []

    for i in range(1, row_count + 1):
        temp_cont = []
        eq = str(input("Enter equation {}'s coefficients: ".format(i)))
        split_int = eq.split()
        for a in split_int:
            temp_cont.append(a)
        for b in range(column_count):
            temp_cont[b] = float(temp_cont[b])

        for x in range(row_count):
            for c in range(column_count):
                print('')
                if x == c:
                    temp_cont.append(float(1))
                else:
                    temp_cont.append(float(0))

        containers.append(temp_cont)
    print('')

    # Creating A Unit Matrix With Same Dimensions

    # Displaying The Main Matrix
    print('Displaying The Augmented Main Matrix:')

    # Print Module
    for i in range(1, row_count + 1):
        print('R{} is    : {} | {}'.format(i, containers[i - 1][0: column_count - 1],
                                           containers[i - 1][column_count - 1:]))
    print('')
