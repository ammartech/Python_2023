def matrix_addition():
    matrix_num = int(input("أدخل عدد المصفوفات: "))
    rows = int(input("أدخل عدد الصفوف: "))
    cols = int(input("أدخل عدد الأعمدة: "))

    matrices = []
    for _ in range(matrix_num):
        print("أدخل عناصر المصفوفة:")
        matrix = []
        for i in range(rows):
            row = []
            for j in range(cols):
                element = float(input(f"أدخل العنصر في الموقع ({i+1}, {j+1}): "))
                row.append(element)
            matrix.append(row)
        matrices.append(matrix)

    result = []
    for i in range(rows):
        row = []
        for j in range(cols):
            sum = 0
            for k in range(matrix_num):
                sum += matrices[k][i][j]
            row.append(sum)
        result.append(row)

    print("النتيجة:")
    display_matrix(result)


def matrix_subtraction():
    rows = int(input("أدخل عدد الصفوف: "))
    cols = int(input("أدخل عدد الأعمدة: "))

    print("أدخل عناصر المصفوفة الأولى:")
    matrix1 = []
    for i in range(rows):
        row = []
        for j in range(cols):
            element = float(input(f"أدخل العنصر في الموقع ({i+1}, {j+1}): "))
            row.append(element)
        matrix1.append(row)

    print("أدخل عناصر المصفوفة الثانية:")
    matrix2 = []
    for i in range(rows):
        row = []
        for j in range(cols):
            element = float(input(f"أدخل العنصر في الموقع ({i+1}, {j+1}): "))
            row.append(element)
        matrix2.append(row)

    result = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(matrix1[i][j] - matrix2[i][j])
        result.append(row)

    print("النتيجة:")
    display_matrix(result)


def matrix_multiplication():
    rows1 = int(input("أدخل عدد الصفوف للمصفوفة الأولى: "))
    cols1 = int(input("أدخل عدد الأعمدة للمصفوفة الأولى: "))
    rows2 = int(input("أدخل عدد الصفوف للمصفوفة الثانية: "))
    cols2 = int(input("أدخل عدد الأعمدة للمصفوفة الثانية: "))

    if cols1 != rows2:
        print("أبعاد غير صالحة لعملية ضرب المصفوفات.")
        return

    print("أدخل عناصر المصفوفة الأولى:")
    matrix1 = []
    for i in range(rows1):
        row = []
        for j in range(cols1):
            element = float(input(f"أدخل العنصر في الموقع ({i+1}, {j+1}): "))
            row.append(element)
        matrix1.append(row)

    print("أدخل عناصر المصفوفة الثانية:")
    matrix2 = []
    for i in range(rows2):
        row = []
        for j in range(cols2):
            element = float(input(f"أدخل العنصر في الموقع ({i+1}, {j+1}): "))
            row.append(element)
        matrix2.append(row)

    result = []
    for i in range(rows1):
        row = []
        for j in range(cols2):
            element = 0
            for k in range(cols1):
                element += matrix1[i][k] * matrix2[k][j]
            row.append(element)
        result.append(row)

    print("النتيجة:")
    display_matrix(result)


def matrix_transpose():
    rows = int(input("أدخل عدد الصفوف: "))
    cols = int(input("أدخل عدد الأعمدة: "))

    print("أدخل عناصر المصفوفة:")
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            element = float(input(f"أدخل العنصر في الموقع ({i+1}, {j+1}): "))
            row.append(element)
        matrix.append(row)

    result = []
    for j in range(cols):
        row = []
        for i in range(rows):
            row.append(matrix[i][j])
        result.append(row)

    print("النتيجة:")
    display_matrix(result)


def matrix_concatenation():
    rows1 = int(input("أدخل عدد الصفوف للمصفوفة الأولى: "))
    cols1 = int(input("أدخل عدد الأعمدة للمصفوفة الأولى: "))
    rows2 = int(input("أدخل عدد الصفوف للمصفوفة الثانية: "))
    cols2 = int(input("أدخل عدد الأعمدة للمصفوفة الثانية: "))

    if rows1 != rows2:
        print("أبعاد غير صالحة لعملية اتحاد المصفوفات.")
        return

    print("أدخل عناصر المصفوفة الأولى:")
    matrix1 = []
    for i in range(rows1):
        row = []
        for j in range(cols1):
            element = float(input(f"أدخل العنصر في الموقع ({i+1}, {j+1}): "))
            row.append(element)
        matrix1.append(row)

    print("أدخل عناصر المصفوفة الثانية:")
    matrix2 = []
    for i in range(rows2):
        row = []
        for j in range(cols2):
            element = float(input(f"أدخل العنصر في الموقع ({i+1}, {j+1}): "))
            row.append(element)
        matrix2.append(row)

    result = []
    for i in range(rows1):
        row = matrix1[i] + matrix2[i]
        result.append(row)

    print("النتيجة:")
    display_matrix(result)


def matrix_inverse():
    n = int(input("أدخل حجم المصفوفة المربعة: "))

    print("أدخل عناصر المصفوفة:")
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            element = float(input(f"أدخل العنصر في الموقع ({i+1}, {j+1}): "))
            row.append(element)
        matrix.append(row)

    determinant = calculate_determinant(matrix)

    if determinant == 0:
        print("المصفوفة غير قابلة للاستدارة.")
        return

    cofactor_matrix = calculate_cofactor_matrix(matrix)
    adjugate_matrix = calculate_adjugate_matrix(cofactor_matrix)

    inverse_matrix = scalar_multiply(adjugate_matrix, 1 / determinant)

    print("النتيجة:")
    display_matrix(inverse_matrix)


def calculate_determinant(matrix):
    n = len(matrix)

    if n == 1:
        return matrix[0][0]

    determinant = 0
    for j in range(n):
        cofactor = (-1) ** j
        sub_matrix = []
        for i in range(1, n):
            row = matrix[i][0:j] + matrix[i][j+1:]
            sub_matrix.append(row)
        determinant += cofactor * matrix[0][j] * calculate_determinant(sub_matrix)

    return determinant


def calculate_cofactor_matrix(matrix):
    n = len(matrix)

    cofactor_matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            cofactor = (-1) ** (i + j)
            sub_matrix = []
            for x in range(n):
                if x != i:
                    sub_row = matrix[x][0:j] + matrix[x][j+1:]
                    sub_matrix.append(sub_row)
            cofactor_value = cofactor * calculate_determinant(sub_matrix)
            row.append(cofactor_value)
        cofactor_matrix.append(row)

    return cofactor_matrix


def calculate_adjugate_matrix(matrix):
    n = len(matrix)

    adjugate_matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(matrix[j][i])
        adjugate_matrix.append(row)

    return adjugate_matrix


def scalar_multiply(matrix, scalar):
    result = []
    for row in matrix:
        new_row = [element * scalar for element in row]
        result.append(new_row)
    return result


def display_matrix(matrix):
    for row in matrix:
        print(row)


def main():
    while True:
        print("قائمة عمليات المصفوفات:")
        print("1. جمع المصفوفات")
        print("2. طرح المصفوفات")
        print("3. ضرب المصفوفات")
        print("4. استدارة المصفوفة")
        print("5. اتحاد المصفوفات")
        print("6. استدارة معكوسة للمصفوفة")
        print("7. الخروج")

        choice = int(input("أدخل اختيارك: "))

        if choice == 1:
            matrix_addition()
        elif choice == 2:
            matrix_subtraction()
        elif choice == 3:
            matrix_multiplication()
        elif choice == 4:
            matrix_transpose()
        elif choice == 5:
            matrix_concatenation()
        elif choice == 6:
            matrix_inverse()
        elif choice == 7:
            break
        else:
            print("اختيار غير صالح. يرجى المحاولة مرة أخرى.")

if __name__ == '__main__':
    main()
