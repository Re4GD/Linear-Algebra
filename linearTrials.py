from linearOperations.Matrix_Operations import *
from linearOperations import Func_3x3_Fix_Var_Gauss_Elimination
from linearOperations import Func_3x3_Fix_Var_Gauss_Jordan_Elimination
from linearOperations import Func_Row_Echelon
from linearOperations import Func_Reduced_Row_Echelon
from linearOperations import Func_Inverse_Method

"""
Kare matrixler
gauss yok etme --> DONE
gauss jordan yok etme --> DONE
cramer
a-1 yardimiyla cozme --> TO DO 
satirca eselon --> DONE
satirca indiegenmis eselon --> DONE

kare olmayan matrixler
satirca eselon --> DONE
satirca indirgenmis eselon --> DONE
"""

menu_intro = """
Usable Operations:

Functions:
3x3 Fix Variable Gauss Elimination Method (3x3 g fix)
3x3 Fix Variable Gauss Jordan Elimination Method (3x3 gj fix)
Max 6x6 Row Echelon Form (ref)
Max 6x6 Reduced Row Echelon Form (rref)

2 Matrix Operations:
Addition (add)
Subtraction (sub)
Multiplication (mult)
Division (div)
Square Root (sqrt)
Dot Product (dot)

1 Matrix Operations:
Transpose (trans)
Inverse (inv2, inv3, inv4) --> inv3 and inv4 NOT DONE
Determinants (det2, det3, det4)

Type 'stop' to stop lines.

Quit (quit)
"""

print(menu_intro)
menu_input = str(input("Select Operation: "))
print('')

while menu_input != 'quit':
    # Menu
    if menu_input.lower() == 'menu':
        print(menu_intro)

    # Transpose
    elif menu_input.lower() == 'trans':
        # Set Random Value
        double = Operations(0, 0)

        # Input Single Matrix
        double.input_matrix1()

        # Display Single Matrix
        print("Displaying The Original Matrix: ")
        print(double.get_matrix1())
        print('')

        # Transpose
        print('Result: (Transpose)')
        print(double.calculate_transpose())
        print('')

    # Inverse 2x2
    elif menu_input.lower() == 'inv2':
        # Set Random Value
        double = Operations(0, 0)

        # Input Single Matrix
        double.input_matrix1()

        # Display Single Matrix
        print("Displaying The Original Matrix: ")
        print(double.get_matrix1())
        print('')

        # Dimension Detect and Get Dot Product
        if double.dimension_fit_inv():
            print('Result: (Inverse)')
            print(double.calculate_inverse2())
            print('')
        else:
            print('Dimensions Of The Matrices Are Not Valid For Inverse!')
            print('')

    # Inverse 3x3
    elif menu_input.lower() == 'inv3':
        # Set Random Value
        double = Operations(0, 0)

        # Input Single Matrix
        double.input_matrix1()

        # Display Single Matrix
        print("Displaying The Original Matrix: ")
        print(double.get_matrix1())
        print('')

        # Dimension Detect and Get Dot Product
        if double.dimension_fit_inv():
            print('Result: (Inverse)')
            print(double.calculate_inverse3())
            print('')
        else:
            print('Dimensions Of The Matrices Are Not Valid For Inverse!')
            print('')

    # Inverse 4x4
    elif menu_input.lower() == 'inv4':
        # Set Random Value
        double = Operations(0, 0)

        # Input Single Matrix
        double.input_matrix1()

        # Display Single Matrix
        print("Displaying The Original Matrix: ")
        print(double.get_matrix1())
        print('')

        # Dimension Detect and Get Dot Product
        if double.dimension_fit_inv():
            print('Result: (Inverse)')
            print(double.calculate_inverse4())
            print('')
        else:
            print('Dimensions Of The Matrices Are Not Valid For Inverse!')
            print('')

    # Determinant 2x2
    elif menu_input.lower() == 'det2':
        # Set Random Value
        double = Operations(0, 0)

        # Input Single Matrix
        double.input_matrix1()

        # Display Single Matrix
        print("Displaying The Original Matrix: ")
        print(double.get_matrix1())
        print('')

        # Dimension Detect and Get Determinant
        if double.dimension_fit_det():
            print('Result: (Determinant)')
            print(double.calculate_determinant2())
            print('')
        else:
            print('Dimensions Of The Matrices Are Not Valid For Determinant!')
            print('')

    # Determinant 3x3
    elif menu_input.lower() == 'det3':
        # Set Random Value
        double = Operations(0, 0)

        # Input Single Matrix
        double.input_matrix1()

        # Display Single Matrix
        print("Displaying The Original Matrix: ")
        print(double.get_matrix1())
        print('')

        # Dimension Detect and Get Determinant
        if double.dimension_fit_det():
            print('Result: (Determinant)')
            print(double.calculate_determinant3())
            print('')
        else:
            print('Dimensions Of The Matrices Are Not Valid For Determinant!')
            print('')

    # Determinant 4x4
    elif menu_input.lower() == 'det4':
        # Set Random Value
        double = Operations(0, 0)

        # Input Single Matrix
        double.input_matrix1()

        # Display Single Matrix
        print("Displaying The Original Matrix: ")
        print(double.get_matrix1())
        print('')

        # Dimension Detect and Get Determinant
        if double.dimension_fit_det():
            print('Result: (Determinant)')
            print(double.calculate_determinant4())
            print('')
        else:
            print('Dimensions Of The Matrices Are Not Valid For Determinant!')
            print('')

    # 3x3 Fix Variable Gauss Elimination Method
    elif menu_input.lower() == '3x3 g fix':
        try:
            Func_3x3_Fix_Var_Gauss_Elimination.gauss_fix_elimination()
        except NameError:
            print('This Module Is Not Available! \n')

    # 3x3 Fix Variable Gauss Jordan Elimination Method
    elif menu_input.lower() == '3x3 gj fix':
        try:
            Func_3x3_Fix_Var_Gauss_Jordan_Elimination.gauss_jordan_fix_elimination()
        except NameError:
            print('This Module Is Not Available! \n')

    # Row Echelon Form Max Dimensions 6x6
    elif menu_input.lower() == 'ref':
        try:
            Func_Row_Echelon.echelon_maker()
        except NameError:
            print('This Module Is Not Available! \n')

    # Reduced Row Echelon Form Max Dimensions 6x6
    elif menu_input.lower() == 'rref':
        try:
            Func_Reduced_Row_Echelon.reduced_echelon_maker()
        except NameError:
            print('This Module Is Not Available! \n')

    # Inverse Method Max Dimensions 6x6
    elif menu_input.lower() == 'finv':
        try:
            Func_Inverse_Method.inverse_method()
        except NameError:
            print('This Module Is Not Available! \n')

    # Addition
    elif menu_input.lower() == 'add':

        # Set Random Value
        double = Operations(0, 0)

        # Input Matrices
        double.input_matrix1()
        double.input_matrix2()

        # Displaying Matrices
        print("Displaying The Original Matrices: ")
        print(double.get_matrix1())
        print('')
        print(double.get_matrix2())
        print('')

        # Dimension Detect and Add
        if double.dimension_fit():
            print('Result: (Addition)')
            print(double.calculate_addition())
            print('')
        else:
            print('Dimensions Of The Matrices Are Not The Same! Cannot Do Addition.')
            print('')

    # Subtraction
    elif menu_input.lower() == 'sub':

        # Set Random Value
        double = Operations(0, 0)

        # Input Matrices
        double.input_matrix1()
        double.input_matrix2()

        # Displaying Matrices
        print("Displaying The Original Matrices: ")
        print(double.get_matrix1())
        print('')
        print(double.get_matrix2())
        print('')

        # Dimension Detect and Subtract
        if double.dimension_fit():
            print('Result: (Subtraction)')
            print(double.calculate_subtraction())
            print('')
        else:
            print('Dimensions Of The Matrices Are Not The Same! Cannot Do Subtract.')
            print('')

    # Multiplication
    elif menu_input.lower() == 'mult':

        # Set Random Value
        double = Operations(0, 0)

        # Input Matrices
        double.input_matrix1()
        double.input_matrix2()

        # Displaying Matrices
        print("Displaying The Original Matrices: ")
        print(double.get_matrix1())
        print('')
        print(double.get_matrix2())
        print('')

        # Dimension Detect and Multiply
        if double.dimension_fit():
            print('Result: (Multiplication)')
            print(double.calculate_multiplication())
            print('')
        else:
            print('Dimensions Of The Matrices Are Not The Same! Cannot Do Multiplication.')
            print('')

    # Division
    elif menu_input.lower() == 'div':

        # Set Random Value
        double = Operations(0, 0)

        # Input Matrices
        double.input_matrix1()
        double.input_matrix2()

        # Displaying Matrices
        print("Displaying The Original Matrices: ")
        print(double.get_matrix1())
        print('')
        print(double.get_matrix2())
        print('')

        # Dimension Detect and Divide
        if double.dimension_fit():
            print('Result: (Division)')
            print(double.calculate_division())
            print('')
        else:
            print('Dimensions Of The Matrices Are Not The Same! Cannot Do Division.')
            print('')

    # Square Root
    elif menu_input.lower() == 'sqrt':
        # Set Random Value
        double = Operations(0, 0)

        # Input Single Matrix
        double.input_matrix1()

        # Display Single Matrix
        print("Displaying The Original Matrix: ")
        print(double.get_matrix1())
        print('')

        # Square Root

        print('Result: (Square Root)')
        print(double.calculate_sqrt())
        print('')

    # Dot Product
    elif menu_input.lower() == 'dot':

        # Set Random Value
        double = Operations(0, 0)

        # Input Matrices
        double.input_matrix1()
        double.input_matrix2()

        # Displaying Matrices
        print("Displaying The Original Matrices: ")
        print(double.get_matrix1())
        print('')
        print(double.get_matrix2())
        print('')

        # Dimension Detect and Get Dot Product
        if double.dimension_fit_dot():
            print('Result: (Dot Product)')
            print(double.calculate_dot())
            print('')
        else:
            print('Dimensions Of The Matrices Are Not Valid For Dot Product!')
            print('')

    # Invalid Input
    else:
        print('Invalid Input!')
        print('')

    menu_input = str(input("Select Operation: "))
    print('')

print('Closing.')
