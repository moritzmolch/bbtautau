

# dummy `requires` decorator
def requires(*args, **kwargs):
    def decorator(func):
        def wrapper(*func_args, **func_kwargs):
            return func(*func_args, **func_kwargs)
        return wrapper
    return decorator

