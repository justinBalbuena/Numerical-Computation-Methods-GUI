from functions.Ant.numerical_diff.lagrange_interpolation import Lagrange
def PtsFwdAndCenter(value_x, x, f, h, flag, type_f):
    n = len(x)
    temp = x.copy()
    temp_f = f.copy()
    less = 0
    greater = 0
    for i in range(n):
        if temp[i] > value_x:
            greater += 1
        else:
            less += 1
    if n > 4 and type_f == "Quadratic":
        type_f = "Cubic"
    if n < 3 and type_f == "Cubic":
        type_f = "Quadratic"
    if type_f == "Quadratic":
        while n > 3:
            if less > greater:
                temp.pop(0)
                less -= 1
            else:
                temp.pop()
                greater -= 1
            n = len(temp)

    if type_f == "Cubic":
        while n > 4:
            if less > greater:
                temp.pop(0)
                temp_f.pop(0)
                less -= 1
            else:
                temp.pop()
                temp_f.pop()
                greater -= 1
            n = len(temp)

    match flag:
        case "a":
            answer = Lagrange(value_x + h, temp, temp_f) - Lagrange(value_x, temp, temp_f)
            answer /= h
            return answer
        case "b":
            answer = (-1 * Lagrange(value_x + 2 * h, temp, temp_f) + 4 * Lagrange(value_x + h, temp,
                                                                                  temp_f) - 3 * Lagrange(value_x, temp,
                                                                                                         temp_f))
            answer /= 2 * h
            return answer
        case "c":
            answer = Lagrange(value_x + h, temp, temp_f) - Lagrange(value_x - h, temp, temp_f)
            answer /= 2 * h
            return answer

