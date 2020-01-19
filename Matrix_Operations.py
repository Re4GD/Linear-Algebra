import numpy
from sympy import Matrix

# 2 Matrix Operations
# Addition / Subtraction / Multiplication / Division ----> Done
# Dot Product ----> Done
# Elementary Matrices ---->
# Transpose / Inverse ----> Done
# Inverse Matrix Solve
#


class Operations(object):
    # __init__
    def __init__(self, m1, m2):
        self.matrix1 = m1
        self.matrix2 = m2

    # Main Operations
    def get_matrix1(self):
        return self.matrix1

    def get_matrix2(self):
        return self.matrix2

    def input_matrix1(self):
        eq1 = ''
        counter1 = 1
        m1 = []

        while eq1 != 'stop':
            temp_cont = []
            eq1 = str(input("Enter coefficients of Equation {} of Matrix 1: ".format(counter1)))
            if eq1 == 'stop':
                break
            x = eq1.split()
            # print(x)
            for j in x:
                temp_cont.append(j)
            m1.append(temp_cont)

            counter1 += 1

        print('')

        np_m1 = numpy.array(m1, dtype=numpy.float64)

        self.matrix1 = np_m1

    def input_matrix2(self):
        eq2 = ''
        counter2 = 1
        m2 = []

        while eq2 != 'stop':
            temp_cont = []
            eq2 = str(input("Enter coefficients of Equation {} of Matrix 2: ".format(counter2)))
            if eq2 == 'stop':
                break
            y = eq2.split()
            # print(x)
            for j in y:
                temp_cont.append(j)
            m2.append(temp_cont)

            counter2 += 1

        print('')

        np_m2 = numpy.array(m2, dtype=numpy.float64)

        self.matrix2 = np_m2

    # Addition / Subtraction / Multiplication / Division / Dimension Control
    def calculate_addition(self):
        sum_matrix = numpy.add(self.matrix1, self.matrix2)
        return sum_matrix

    def calculate_subtraction(self):
        sub_matrix = numpy.subtract(self.matrix1, self.matrix2)
        return sub_matrix

    def calculate_multiplication(self):
        mult_matrix = numpy.multiply(self.matrix1, self.matrix2)
        return mult_matrix

    def calculate_division(self):
        div_matrix = numpy.divide(self.matrix1, self.matrix2)
        return div_matrix

    def calculate_sqrt(self):
        sqrt_matrix = numpy.sqrt(self.matrix1)
        return sqrt_matrix

    def dimension_fit(self):
        # Dimension Control For Addition / Subtraction / Multiplication / Division
        if self.matrix1.shape == self.matrix2.shape:
            return True

    # Dot Product / Dimension Control
    def calculate_dot(self):
        dot_matrix = numpy.dot(self.matrix1, self.matrix2)
        return dot_matrix

    def dimension_fit_dot(self):

        col1 = self.matrix1[1, :]
        row2 = self.matrix2[:, 1]

        if col1.shape == row2.shape:
            return True

    # Transpose / Inverse / Dimension Control
    def calculate_transpose(self):
        trans_matrix = self.matrix1.T
        return trans_matrix

    def calculate_inverse2(self):
        det = (self.matrix1[0][0] * self.matrix1[1][1]) - (self.matrix1[0][1] * self.matrix1[1][0])
        self.matrix1[0][0], self.matrix1[1][1] = self.matrix1[1][1], self.matrix1[0][0]
        self.matrix1[0][1] = - self.matrix1[0][1]
        self.matrix1[1][0] = - self.matrix1[1][0]
        if det != 0:
            inv_matrix = numpy.multiply(1 / det, self.matrix1)
            return inv_matrix
        else:
            return 'Determinant of this matrix is 0. There is no inverse!'

    def calculate_inverse3(self):
        pass

    def calculate_inverse4(self):
        pass

    def dimension_fit_inv(self):

        col1 = self.matrix1[:, 1]
        row1 = self.matrix1[1, :]

        if col1.shape == row1.shape:
            return True

    def calculate_determinant2(self):
        determinant = (self.matrix1[0][0] * self.matrix1[1][1]) - (self.matrix1[0][1] * self.matrix1[1][0])
        return determinant

    def calculate_determinant3(self):
        determinant = (self.matrix1[0][0] * self.matrix1[1][1] * self.matrix1[2][2] +
                       self.matrix1[1][0] * self.matrix1[2][1] * self.matrix1[0][2] +
                       self.matrix1[2][0] * self.matrix1[0][1] * self.matrix1[1][2]) - \
                      (self.matrix1[0][2] * self.matrix1[1][1] * self.matrix1[2][0] +
                       self.matrix1[1][2] * self.matrix1[2][1] * self.matrix1[0][0] +
                       self.matrix1[2][2] * self.matrix1[0][1] * self.matrix1[1][0])
        return determinant

    def calculate_determinant4(self):
        cont0 = self.matrix1[0]
        cont1 = self.matrix1[1]
        cont2 = self.matrix1[2]
        cont3 = self.matrix1[3]
        system = Matrix([cont0, cont1, cont2, cont3])
        return system.det()

    def dimension_fit_det(self):

            col1 = self.matrix1[:, 1]
            row1 = self.matrix1[1, :]

            if col1.shape == row1.shape:
                return True
