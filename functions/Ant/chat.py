from sympy import fwht

# sequence
seq = [123,95,721,91,9,8,12,57]

# hwht
transform = fwht(seq)
print("Transform  : ", transform)