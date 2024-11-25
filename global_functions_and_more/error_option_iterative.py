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
    "True root mean square error (RMSE)": true_root_error_method()
}