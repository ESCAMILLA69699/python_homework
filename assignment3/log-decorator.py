
import logging
from functools import wraps

logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log", "a"))


def logger_decorator(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        result = func(*args, **kwargs)

        logger.info(f"function: {func.__name__}")
        logger.info(f"positional parameters: {args if args else 'none'}")
        logger.info(f"keyword parameters: {kwargs if kwargs else 'none'}")
        logger.info(f"return: {result}")
        logger.info("")

        return result

    return wrapper


@logger_decorator
def function_one():
    print("Hello, World!")


@logger_decorator
def function_two(*args):
    return True


@logger_decorator
def function_three(**kwargs):
    return logger_decorator


if __name__ == "__main__":
    function_one()
    function_two(13, 47, 82, 29)
    function_three(name="Alex", age=24)
