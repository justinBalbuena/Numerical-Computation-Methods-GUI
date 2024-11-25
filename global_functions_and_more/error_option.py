#this can be use a key for a st.radio since there are function that ask for there error methods
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