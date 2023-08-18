"""
E1. Cree una función sin recursión de cola que reciba dos matrices mxn y devuelva cuántos elementos iguales tienen.
Los elementos serán iguales si tienen el mismo valor y tienen la misma posición.
"""

"""
def e1(m1, m2):
    if len(m1) != len(m2) or len(m1[0]) != len(m2[0]):
        return None

    f = len(m1)
    c = len(m1[0])
    count = 0

    for i in range(f):
        for j in range(c):
            if m1[i][j] == m2[i][j]:
                count += 1

    return count


# Casos base:
assert (e1([[1, 2, 3, 4], [5, 6, 7, 8], [0, 1, 0, 1]], [[1, 2, 3, 4], [5, 6, 7, 8], [0, 1, 0, 1]]) == 12)
assert (e1([[1, 2], [5, 6], [0, 1]], [[1, 2], [5, 6], [0, 1]]) == 6)
assert (e1([[1, 2], [6, 6], [0, 1]], [[1, 2], [5, 6], [0, 1]]) == 5)
assert (e1([[1, 2], [6, 4]], [[1, 2], [5, 6]]) == 2)
assert (e1([[]], [[]]) == 0)
"""
"""
E2. Escriba una función recursiva de cola que reciba un entero y retorne uno nuevo con sus dígitos pares eliminados.
"""

"""
def e2(n, r=0, f=1):
    if n == 0:
        return r

    digito = n % 10
    if digito % 2 != 0:
        r += digito * f
        f *= 10

    return e2(n // 10, r, f)


# Caso base
assert(e2(543211) == 5311)
assert(e2(1234) == 13)
assert(e2(123124) == 131)
assert(e2(57575757) == 57575757)
assert(e2(1) == 1)
"""

"""
E3. Escriba una función recursiva que reciba un string S y retorne la sumatoria de las posiciones de las ocurrencias de 
un caracter c. Si c no está en S, devuelva -1 --> una ocurrencia es una aparición, así que deben sumarse todas las 
posiciones donde aparece el caracter c.
"""


def e3(string, c, index=0):
    if index >= len(string):
        return 0

    if string[index] == c:
        return index + e3(string, c, index + 1)

    return e3(string, c, index + 1)


assert (e3("camita", "a") == 6)
assert (e3("asdfasdf", "s") == 6)
assert (e3("abcde", "e") == 4)
assert (e3("lasso", "s") == 5)
assert (e3("a", "x") == 0)
print(e3("a", "x"))
print(e3("camita", "a"))
print(e3("asdfasdf", "s"))
print(e3("abcde", "e"))
print(e3("lasso", "s"))
