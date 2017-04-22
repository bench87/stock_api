from functools import wraps
from pymonad import Left, Right


def either_decorator(f):
    @wraps(f)
    def inner(*args, **kwargs):
        try:
            r = f(*args, **kwargs)
            return Right(r)
        except Exception as e:
            return Left(e)
    return inner
