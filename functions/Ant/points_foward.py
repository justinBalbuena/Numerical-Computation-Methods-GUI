from functions.Ant.lagrange_method import ant_lagrange


def append(value_x,x,f,interpol):
    if interpol == "quadratic":
        while len(x) > 3:
            sum_beg = abs(value_x - x[0])
            sum_end = abs(value_x - x[-1])
            if sum_beg > sum_end:
                x.pop(0)
                f.pop(0)
            else:
                x.pop()
                f.pop()
    if interpol == "polynomial":
        while len(x) > 4:
            sum_beg = abs(value_x - x[0])
            sum_end = abs(value_x - x[-1])
            if sum_beg > sum_end:
                x.pop(0)
                f.pop(0)
            else:
                x.pop()
                f.pop()
    return x, f

def PtsFwdAndCenter(value_x, x, f, h, flag,type):
    temp = x.copy()
    temp_f = f.copy()
    temp,temp_f = append(value_x,temp,temp_f,type)
    match flag:
        case "a":
            answer = ant_lagrange(value_x + h, temp, temp_f) - ant_lagrange(value_x, temp, temp_f)
            answer /= h
            return answer
        case "b":
            answer = (-1 * ant_lagrange(value_x + 2 * h, temp, temp_f) + 4 * ant_lagrange(value_x + h, temp,temp_f) - 3 * ant_lagrange(value_x, temp,temp_f))
            answer /= 2 * h
            return answer
        case "c":
            answer = ant_lagrange(value_x + h, temp, temp_f) - ant_lagrange(value_x - h, temp, temp_f)
            answer /= 2 * h
            return answer
