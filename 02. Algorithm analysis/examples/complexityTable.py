import math
from decimal import Decimal
from tabulate import tabulate

print '\nConstant.\nLogarithmic.\nLinear.\nLinearithmic.\nQuadratic\nCubic.\nExponential.\n'

headers = ["n", "O(1)", "O(log(n))", "O(n)", "O(nlog(n))", "O(n^2)", "O(n^3)", "O(2^n)"]
table = []

lst = [2 ** i for i in range(10)]
for i in lst:
	table.append([i, 1, math.log(i, 2), i, i * math.log(i, 2), i ** 2, i ** 3, '%.2E' % Decimal(str(2 ** i))])

print tabulate(table, headers, tablefmt="grid")