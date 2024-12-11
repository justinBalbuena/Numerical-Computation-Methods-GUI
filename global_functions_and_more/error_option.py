#this can be use a key for a st.radio since there are function that ask for there error methods
from numpy.polynomial.polynomial import Polynomial
from scipy.sparse.csgraph import maximum_bipartite_matching


def absolute_error_method():
    return "a"
def relative_error_method():
    return "b"
def true_absolute_error_method():
    return "c"
def combination():
    return "d"

error_tolerance_methods = {
    "Absolute Error": absolute_error_method,
    "Relative Error": relative_error_method,
    "True Absolute Error": true_absolute_error_method,
    "Combination of Absolute Error and Relative Error": combination
}


#this can be use a key for a st.radio since there are function that ask for there error methods
#specifically for the iterative error method
def approx_mean_error_method():
    return "a"
def approx_root_error_method():
    return "b"
def true_mean_error_method():
    return "c"
def true_root_error_method():
    return "d"

error_tolerance_methods_iter = {
    "Approximate mean absolute error (MAE)": approx_mean_error_method,
    "Approximate root mean square error (RMSE)": approx_root_error_method,
    "True mean absolute error (MAE)": true_mean_error_method,
    "True root mean square error (RMSE)": true_root_error_method
}


def polynomial_interpolation():
    return "polynomial"
def quadratic_interpolation():
    return "quadratic"

interpolation_methods = {
    "polynomial interpolation": polynomial_interpolation,
    "quadratic interpolation": quadratic_interpolation
}


def minimum_extrema():
    return "min"
def maximum_extrema():
    return "max"

extrema_types = {
    "Minimum Extrema": minimum_extrema,
    "Maximum Extrema": maximum_extrema
}