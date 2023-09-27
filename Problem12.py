# def get_nth_triangle_num(n):
#     sum_nums = 0
#     for i in range(1, n + 1):
#         sum_nums += i
#     return sum_nums
#
#
# def find_divisors(n):
#     divisors = []
#     for i in range(1, n // 2 + 1):
#         if n % i == 0:
#             divisors.append(i)
#     divisors.append(n)
#     return divisors
#
#
# def get_first_triangle_n_div(amount):
#     i = 1
#     while True:
#         tri_num = get_nth_triangle_num(i)
#         divs = find_divisors(tri_num)
#         print(tri_num, ":", len(divs), ":", divs)
#         if len(divs) >= amount:
#             return tri_num, divs
#         i += 1
#
#
# print(get_nth_triangle_num(28))
# print(get_first_triangle_n_div(500))


from sympy import divisors
import math

_maxDiv = 500
_n = 1
_valTrian = 0

while True:
    _n += 1
    _valTrianPiv = _n * (_n + 1) / 2
    if _valTrianPiv > math.sqrt(_maxDiv):
        divisores = divisors(int(_valTrianPiv))
        _numDiv = len(divisores)
        if _numDiv >= _maxDiv:
            _valTrian = _valTrianPiv
            break

print(_valTrian)
