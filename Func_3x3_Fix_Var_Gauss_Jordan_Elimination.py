from sympy import symbols, solve


def gauss_jordan_fix_elimination():
    # Linear Algebra 3x3 Matrix With 'Fix Matrix Numbers' Solved By Gauss Jordan Elimination Method
    print('')
    print("Linear Algebra 3x3 Matrix With 'Fix Matrix Numbers' Solved By Gauss Jordan Elimination Method")
    print('')
    print("This is an algorithm to find 3x3 Linear Equation Systems by using Gauss Jordan Elimination Method.")
    print("The coefficients of 'x', 'y' and 'z' and the result must be written with a space('') in between.")
    print("The coefficients and the result must be integers, not fractions or irrationals.")
    print('')
    print("Example Input = -1 0 5 9")
    print("Meaning of Example Input = -1x + 5z = 9")
    print('')

    eq1 = str(input("Enter first equation coefficients : "))
    eq2 = str(input("Enter second equation coefficients: "))
    eq3 = str(input("Enter third equation coefficients : "))
    print('')

    # Converting Equations To Lists and Conversion Of All Elements To Floats
    cont1 = []
    cont2 = []
    cont3 = []

    x = eq1.split()
    y = eq2.split()
    z = eq3.split()

    for i in x:
        cont1.append(i)
    for j in y:
        cont2.append(j)
    for k in z:
        cont3.append(k)

    for i in range(4):
        cont1[i] = float(cont1[i])
    for i in range(4):
        cont2[i] = float(cont2[i])
    for i in range(4):
        cont3[i] = float(cont3[i])

    # Displaying The Main Matrix
    print('Displaying The Augmented Main Matrix:')
    print('R1 is    :', cont1[0:3], '|', cont1[3])
    print('R2 is    :', cont2[0:3], '|', cont2[3])
    print('R3 is    : ' + str(cont3[0:3]) + ' | ' + str(cont3[3]) + '\n')

    # Making Sure C1R1 is not 0
    if cont1[0] == 0:
        if cont2[0] != 0:
            cont1, cont2 = cont2, cont1
            print('R1 swapped with R2. \n')
            print('R1 is    :', cont1[0:3], '|', cont1[3])
            print('R2 is now:', cont2[0:3], '|', cont2[3])
            print('R3 is    : ' + str(cont3[0:3]) + ' | ' + str(cont3[3]) + '\n')
        elif cont3[0] != 0:
            cont1, cont3 = cont3, cont1
            print('R1 swapped with R3. \n')
            print('R1 is    :', cont1[0:3], '|', cont1[3])
            print('R2 is    :', cont2[0:3], '|', cont2[3])
            print('R3 is now: ' + str(cont3[0:3]) + ' | ' + str(cont3[3]) + '\n')

    # Making Sure All 0 Rows Go To The Bottom
    if cont2[0] == 0 and cont2[1] == 0 and cont2[2] == 0 and cont2[3] == 0:
        cont2, cont3 = cont3, cont2
        print('R2 swapped with R3. \n')
        print('R1 is    :', cont1[0:3], '|', cont1[3])
        print('R2 is    :', cont2[0:3], '|', cont2[3])
        print('R3 is now: ' + str(cont3[0:3]) + ' | ' + str(cont3[3]) + '\n')

    # Creating Upper Triangular Matrix (C1R2)
    if cont2[0] == 0:
        print('First Column / Second Row is already 0. \n')
    elif cont2[0] != 0:
        multiplyer_c1_r2 = -(float(cont2[0]) / float(cont1[0]))
        cont2[0] = multiplyer_c1_r2 * float(cont1[0]) + float(cont2[0])
        cont2[1] = multiplyer_c1_r2 * float(cont1[1]) + float(cont2[1])
        cont2[2] = multiplyer_c1_r2 * float(cont1[2]) + float(cont2[2])
        cont2[3] = multiplyer_c1_r2 * float(cont1[3]) + float(cont2[3])
        print(str(multiplyer_c1_r2) + ' R1 + R2 ---> R2 \n')
        print('R1 is    :', cont1[0:3], '|', cont1[3])
        print('R2 is    :', cont2[0:3], '|', cont2[3])
        print('R3 is    : ' + str(cont3[0:3]) + ' | ' + str(cont3[3]) + '\n')

    # Creating Upper Triangular Matrix (C1R3)
    if cont3[0] == 0:
        print('First Column / Third Row is already 0. \n')
    elif cont3[0] != 0:
        multiplyer_c1_r3 = -(float(cont3[0]) / float(cont1[0]))
        cont3[0] = multiplyer_c1_r3 * float(cont1[0]) + float(cont3[0])
        cont3[1] = multiplyer_c1_r3 * float(cont1[1]) + float(cont3[1])
        cont3[2] = multiplyer_c1_r3 * float(cont1[2]) + float(cont3[2])
        cont3[3] = multiplyer_c1_r3 * float(cont1[3]) + float(cont3[3])
        print(str(multiplyer_c1_r3) + ' R1 + R3 ---> R3 \n')
        print('R1 is    :', cont1[0:3], '|', cont1[3])
        print('R2 is    :', cont2[0:3], '|', cont2[3])
        print('R3 is    : ' + str(cont3[0:3]) + ' | ' + str(cont3[3]) + '\n')

    # Making Sure C2R2 is not 0
    if cont2[1] == 0 and cont3[0] == 0:
        cont2, cont3 = cont3, cont2
        print('R2 swapped with R3. \n')
        print('R1 is    :', cont1[0:3], '|', cont1[3])
        print('R2 is now:', cont2[0:3], '|', cont2[3])
        print('R3 is    : ' + str(cont3[0:3]) + ' | ' + str(cont3[3]) + '\n')

    # Creating Upper Triangular Matrix (C2R3)
    if cont3[1] == 0:
        print('Second Column / Third Row is already 0. \n')
    elif cont3[1] != 0:
        multiplyer_c2_r3 = -(float(cont3[1]) / float(cont2[1]))
        cont3[1] = multiplyer_c2_r3 * float(cont2[1]) + float(cont3[1])
        cont3[2] = multiplyer_c2_r3 * float(cont2[2]) + float(cont3[2])
        cont3[3] = multiplyer_c2_r3 * float(cont2[3]) + float(cont3[3])
        print(str(multiplyer_c2_r3) + ' R2 + R3 ---> R3 \n')
        print('R1 is    :', cont1[0:3], '|', cont1[3])
        print('R2 is    :', cont2[0:3], '|', cont2[3])
        print('R3 is    : ' + str(cont3[0:3]) + ' | ' + str(cont3[3]) + '\n')

    print('Upper Triangular Matrix is formed. \n')

    # Creating Lower Triangular Matrix (C3R2)
    if cont3[2] == 0:
        print('Third Column / Third Row is 0, cannot operate for R2. \n')
    else:
        if cont2[2] == 0:
            print('Third Column / Second Row is already 0. \n')
        elif cont2[2] != 0:
            multiplyer_c3_r2 = -(float(cont2[2]) / float(cont3[2]))
            cont2[2] = multiplyer_c3_r2 * float(cont3[2]) + float(cont2[2])
            cont2[3] = multiplyer_c3_r2 * float(cont3[3]) + float(cont2[3])
            print(str(multiplyer_c3_r2) + ' R1 + R2 ---> R2 \n')
            print('R1 is    :', cont1[0:3], '|', cont1[3])
            print('R2 is    :', cont2[0:3], '|', cont2[3])
            print('R3 is    : ' + str(cont3[0:3]) + ' | ' + str(cont3[3]) + '\n')

    # Creating Lower Triangular Matrix (C3R1)
    if cont3[2] == 0:
        print('Third Column / Third Row is 0, cannot operate for R1. \n')
    else:
        if cont1[2] == 0:
            print('Third Column / First Row is already 0. \n')
        elif cont1[2] != 0:
            multiplyer_c3_r1 = -(float(cont1[2]) / float(cont3[2]))
            cont1[2] = multiplyer_c3_r1 * float(cont3[2]) + float(cont1[2])
            cont1[3] = multiplyer_c3_r1 * float(cont3[3]) + float(cont1[3])
            print(str(multiplyer_c3_r1) + ' R1 + R2 ---> R2 \n')
            print('R1 is    :', cont1[0:3], '|', cont1[3])
            print('R2 is    :', cont2[0:3], '|', cont2[3])
            print('R3 is    : ' + str(cont3[0:3]) + ' | ' + str(cont3[3]) + '\n')

    # Creating Lower Triangular Matrix (C2R1)
    if cont2[1] == 0:
        print('Second Column / Second Row is 0, cannot operate for R1. \n')
    else:
        if cont1[1] == 0:
            print('Second Column / First Row is already 0. \n')
        elif cont1[1] != 0:
            multiplyer_c2_r1 = -(float(cont1[1]) / float(cont2[1]))
            cont1[1] = multiplyer_c2_r1 * float(cont2[1]) + float(cont1[1])
            cont1[3] = multiplyer_c2_r1 * float(cont2[3]) + float(cont1[3])
            print(str(multiplyer_c2_r1) + ' R1 + R2 ---> R2 \n')
            print('R1 is    :', cont1[0:3], '|', cont1[3])
            print('R2 is    :', cont2[0:3], '|', cont2[3])
            print('R3 is    : ' + str(cont3[0:3]) + ' | ' + str(cont3[3]) + '\n')

    print('Lower Triangular Matrix is formed. \n')
    print('Displaying The Final Augmented Matrix:')
    print('R1 is    :', cont1[0:3], '|', cont1[3])
    print('R2 is    :', cont2[0:3], '|', cont2[3])
    print('R3 is    : ' + str(cont3[0:3]) + ' | ' + str(cont3[3]) + '\n')

    # Guessing The Answer Of The Last Matrix (Unique Answer/ Infinite Answers/ No Answer)
    # Unique Answer
    if float(cont3[0]) == 0 and float(cont3[1]) == 0 and float(cont3[2]) != 0:

        var3 = float(cont3[3]) / float(cont3[2])
        var2 = (float(cont2[3]) - (float(cont2[2]) * var3)) / float(cont2[1])
        var1 = (float(cont1[3]) - float(cont1[2] * var3) - float(cont1[1] * var2)) / float(cont1[0])

        print('The answer for this 3x3 Matrix is:')
        print('(x, y, z) = (' + str(var1) + ', ' + str(var2) + ', ' + str(var3) + ')')
        print('')

    # Infinite Answer
    is_x_free = False
    is_y_free = False
    is_z_free = False

    if float(cont3[0]) == 0 and float(cont3[1]) == 0 and float(cont3[2]) == 0 and float(cont3[3]) == 0:
        print('There are infinite solutions to this matrix.')
        if cont1[0] != 0:
            print('x is a basic variable.')
        elif cont1[0] == 0:
            print('x is a free variable.')
            is_x_free = True
        if cont2[1] != 0:
            print('y is a basic variable.')
        elif cont2[1] == 0:
            print('y is a free variable.')
            is_y_free = True
        if cont3[2] != 0:
            print('z is a basic variable.')
        elif cont3[2] == 0:
            print('z is a free variable.')
            is_z_free = True

        print('')

        a, b, c, x, y, z = symbols('a b c x y z')
        var_x = x
        var_y = y
        var_z = z
        result_x = 0
        result_y = 0
        result_z = 0

        if is_x_free:
            print('Let x = a')
            var_x = a
            result_x = var_x
        if is_y_free:
            print('Let y = b')
            var_y = b
            result_y = var_y
        if is_z_free:
            print('Let z = c')
            var_z = c
            result_z = var_z

        if not is_y_free:
            result_y = solve(float(cont2[1]) * var_y + float(cont2[2]) * var_z - float(cont2[3]), y)
            var_y = result_y[0]
        if not is_x_free:
            result_x = solve(float(cont1[0]) * var_x + float(cont1[1]) * var_y + float(cont1[2]) * var_z -
                             float(cont1[3]), x)

        print('')
        print('The answer for this 3x3 Matrix is:')
        print('(x, y, z) = (' + str(result_x[0]) + ', ' + str(result_y[0]) + ', ' + str(result_z) + ')')
        print('')

    # No Answer
    if float(cont3[0]) == 0 and float(cont3[1]) == 0 and float(cont3[2]) == 0 and float(cont3[3]) != 0:
        print('There is no solution to this matrix.')
        print('')
