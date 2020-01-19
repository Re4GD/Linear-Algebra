from sympy import symbols, solve_linear_system, Matrix


def reduced_echelon_maker():
    # Linear Algebra Matrix With Maximum 6x6 Dimensions Solved By Reduced Row Echelon Form
    print('')
    print("Linear Algebra Matrix With Maximum 6x6 Dimensions Solved By Reduced Row Echelon Form")
    print('')
    print("This is an algorithm to solve Linear Equation Systems by using Reduced Row Echelon Form.")
    print("The coefficients of 'x', 'y', 'z', etc. and the result must be written with a space('') in between.")
    print("The coefficients and the result must be integers, not fractions or irrationals.")
    print('')
    print('Example Dimensions (Row/Column)= 4 3')
    print("Example Input = -1 0 5 9")
    print("Meaning of Example Input = -1x + 5z = 9")
    print('')

    # Converting Equations To Lists and Conversion Of All Elements To Floats
    dimensions = str(input('Enter Dimensions Of The Matrix: '))
    print('')

    d_list = dimensions.split()
    row_count = d_list[0]
    column_count = d_list[1]

    while int(row_count) > 6 or int(column_count) > 7:
        print('Max Dimensions Are 6 Rows And 6 Columns!')
        print('')
        dimensions = str(input('Enter Dimensions Of The Matrix: '))
        d_list = dimensions.split()
        row_count = d_list[0]
        column_count = d_list[1]

    row_count = int(row_count)
    column_count = int(column_count)
    containers = []

    for i in range(1, row_count + 1):
        temp_cont = []
        eq = str(input("Enter equation {}'s coefficients: ".format(i)))
        split_int = eq.split()
        for a in split_int:
            temp_cont.append(a)
        for b in range(column_count):
            temp_cont[b] = float(temp_cont[b])
        containers.append(temp_cont)
    print('')

    # Displaying The Main Matrix
    print('Displaying The Augmented Main Matrix:')

    # Print Module
    for i in range(1, row_count + 1):
        print('R{} is    : {} | {}'.format(i, containers[i - 1][0: column_count - 1],
                                           containers[i - 1][column_count - 1:]))
    print('')

    # Detecting All 0 Rows And Making Them Go To The Bottom
    zeros = []
    non_zeros = []
    for row in range(row_count):
        is_zero = 0
        for column in range(column_count):
            if containers[row][column] == 0:
                is_zero += 1
        if is_zero == column_count:
            zeros.append(row)
        else:
            non_zeros.append(row)

    divided_containers = []
    for i in non_zeros:
        divided_containers.append(containers[i])
    for i in zeros:
        divided_containers.append(containers[i])

    containers = divided_containers

    print('Making All 0 Rows Go To The Bottom')

    # Print Module
    for i in range(1, row_count + 1):
        print('R{} is    : {} | {}'.format(i, containers[i - 1][0: column_count - 1],
                                           containers[i - 1][column_count - 1:]))
    print('')

    column_number = 0
    row_number = 0

    while column_number < column_count and row_number < row_count:
        # Making Sure First Element Is Not Zero
        for counter_y in range(row_number, row_count):

            if containers[row_number][column_number] != 0:
                break
            elif containers[counter_y][column_number] != 0 and counter_y != row_number:
                print('R{} swapped with R{}.'.format(counter_y + 1, row_number + 1))
                containers[counter_y], containers[row_number] = containers[row_number], containers[counter_y]

                # Print Module
                for i in range(1, row_count + 1):
                    print('R{} is    : {} | {}'.format(i, containers[i - 1][0: column_count - 1],
                                                       containers[i - 1][column_count - 1:]))
                print('')

        # Making 1
        if containers[row_number][column_number] == 0 and column_number + 1 != column_count - 1:
            column_number += 1

        if containers[row_number][column_number] == 1:
            print('Column {} / Row {} is already 1. \n'.format(row_number + 1, column_number + 1))

        elif containers[row_number][column_number] != 1:
            try:
                multiplyer_one = (1 / float(containers[row_number][column_number]))

                for i in range(0, column_count):
                    containers[row_number][i] = multiplyer_one * float(containers[row_number][i])

                print(str(multiplyer_one) + ' R{} ---> R{} \n'.format(row_number + 1, row_number + 1))
            except ZeroDivisionError:
                print('Column {} / Row {} is already 0. \n'.format(row_number + 1, column_number + 1))

            # Print Module
            for i in range(1, row_count + 1):
                print('R{} is    : {} | {}'.format(i, containers[i - 1][0: column_count - 1],
                                                   containers[i - 1][column_count - 1:]))
            print('')

        # Making Below And Above 0
        if row_number < row_count:
            print('Making Below And Above C{}R{} All 0'.format(column_number + 1, row_number + 1))
            for i in range(0, row_count):
                if containers[i][column_number] != 0:
                    multiplyer_zero = -(float(containers[i][column_number]))
                    for j in range(0, column_count):
                        if i != row_number:
                            containers[i][j] = multiplyer_zero * float(containers[row_number][j]) + \
                                               float(containers[i][j])
            # Print Module
            for i in range(1, row_count + 1):
                print('R{} is    : {} | {}'.format(i, containers[i - 1][0: column_count - 1],
                                                   containers[i - 1][column_count - 1:]))
            print('')

        column_number += 1
        row_number += 1

    # Create Containers And Fill Them
    cont0 = []
    cont1 = []
    cont2 = []
    cont3 = []
    cont4 = []
    cont5 = []

    try:
        cont0 = containers[0]
        cont1 = containers[1]
        cont2 = containers[2]
        cont3 = containers[3]
        cont4 = containers[4]
        cont5 = containers[5]
    except IndexError:
        pass

    # Add 0 To Empty Containers
    x, y, z, t, v, w = symbols('x y z t v w')
    result_str = '('

    if len(cont0) == 0:
        for i in range(column_count):
            cont0.append(float(0))

    if len(cont1) == 0:
        for i in range(column_count):
            cont1.append(float(0))

    if len(cont2) == 0:
        for i in range(column_count):
            cont2.append(float(0))

    if len(cont3) == 0:
        for i in range(column_count):
            cont3.append(float(0))

    if len(cont4) == 0:
        for i in range(column_count):
            cont4.append(float(0))

    if len(cont5) == 0:
        for i in range(column_count):
            cont5.append(float(0))

    var_count = column_count - 1

    if var_count == 6:
        result_str += 'x, y, z, t, v, w'
        pass
    elif var_count == 5:
        result_str += 'x, y, z, t, v'
        w = 0
    elif var_count == 4:
        result_str += 'x, y, z, t'
        w = v = 0
    elif var_count == 3:
        result_str += 'x, y, z'
        w = v = t = 0
    elif var_count == 2:
        result_str += 'x, y'
        w = v = t = z = 0
    elif var_count == 1:
        result_str += 'x'
        w = v = t = z = y = 0

    result_str += ') = ('

    # Guessing The Answer Of The Last Matrix (Unique Answer/ Infinite Answers/ No Answer)
    system = Matrix([cont0, cont1, cont2, cont3, cont4, cont5])
    result = solve_linear_system(system, x, y, z, t, v, w)

    # No Answer
    if result is None:
        print('There is no solution to this matrix.')
        print('')
    else:
        # Unique Answer / Infinite Answer
        if 'x' in result_str:
            try:
                result_str += '{}'.format(result[x])
                print('x is a basic variable.')
            except KeyError:
                result_str += 'x'
                print('x is a free variable.')

        if 'y' in result_str:
            try:
                result_str += ', {}'.format(result[y])
                print('y is a basic variable.')
            except KeyError:
                result_str += ', y'
                print('y is a free variable.')

        if 'z' in result_str:
            try:
                result_str += ', {}'.format(result[z])
                print('z is a basic variable.')
            except KeyError:
                result_str += ', z'
                print('z is a free variable.')

        if 't' in result_str:
            try:
                result_str += ', {}'.format(result[t])
                print('t is a basic variable.')
            except KeyError:
                result_str += ', t'
                print('t is a free variable.')

        if 'v' in result_str:
            try:
                result_str += ', {}'.format(result[v])
                print('v is a basic variable.')
            except KeyError:
                result_str += ', v'
                print('v is a free variable.')

        if 'w' in result_str:
            try:
                result_str += ', {}'.format(result[w])
                print('w is a basic variable.')
            except KeyError:
                result_str += ', w'
                print('w is a free variable.')

        result_str += ')'
        print('')
        print(result_str)
        print('')
