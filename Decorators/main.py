# import time
#
# def timer(func):
#     def wrapper(*args):
#         start_time = time.time()
#         result = func(*args)
#         end_time = time.time()
#         print(f"{func.__name__} took {round(end_time - start_time, 3)} seconds to execute")
#         return result
#     return wrapper
#
# @timer
# def make_list(length):
#     return [i for i in range(length)]
#
# make_list(10000)
# make_list(100000)
# make_list(1000000)

# ================================================================================================================

# def cache(func):
#     cached_results = {}
#
#     def wrapper(*args):
#         if args in cached_results:
#             return cached_results[args]
#         result = func(*args)
#         cached_results[args] = result
#         return result
#     return  wrapper
#
# @cache
# def fibo(n):
#     if n == 0 or n == 1:
#         return 1
#     return fibo(n - 1) + fibo(n - 2)
#
# print(fibo(25))

# ================================================================================================================

def validate_args(*types):
    def decorator(func):
        def wrapper(*args):
            for arg, arg_type in zip(args, types):
                if not isinstance(arg, arg_type):
                    raise TypeError(f"Expected {arg_type}, got {type(arg)}")
            return func(*args)
        return wrapper
    return decorator

@validate_args(int, int)
def sum_string(first, second):
    return first + second

print(sum_string(3, 8))