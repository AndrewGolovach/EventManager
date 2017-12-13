import sys
import functools
import logging
import traceback

import collections

INCORRECT_EXCEPTION_TYPE_MESSAGE = "exc_type should extend Exception or be non-empty tuple of Exception subclasses"


def handle_error(re_raise=True, log_traceback=True, exc_type=Exception):
    assert_exception_extends_type(exc_type, Exception)

    def wrapper(f):
        @functools.wraps(f)
        def wrapped(*args, **kwargs):
            try:
                return f(*args, **kwargs)
            except:
                handle_raised_error(re_raise, log_traceback, exc_type, *sys.exc_info())
        return wrapped
    return wrapper


class handle_error_context(object):
    def __init__(self, re_raise=True, log_traceback=True, exc_type=Exception):
        assert_exception_extends_type(exc_type, Exception)

        self.re_raise = re_raise
        self.log_traceback = log_traceback
        self.exc_type = exc_type

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_instance, exc_traceback):
        if exc_instance is None:
            pass
        else:
            handle_raised_error(self.re_raise, self.log_traceback, self.exc_type, exc_type, exc_instance, exc_traceback)


def assert_exception_extends_type(exc_type, exc_supertype):
    assert (not isinstance(exc_type, tuple) and issubclass(exc_type, exc_supertype)) or \
           (isinstance(exc_type, tuple) and all(issubclass(t, exc_supertype) for t in exc_type)), \
        INCORRECT_EXCEPTION_TYPE_MESSAGE


def handle_raised_error(re_raise, log_traceback, expected_exc_type, exc_type, exc_instance, exc_traceback):
    print exc_type, expected_exc_type
    if (not isinstance(exc_type, tuple) and issubclass(exc_type, expected_exc_type)) or \
            (isinstance(expected_exc_type, collections.Iterable) and exc_type in expected_exc_type):

        if log_traceback:
            logging.error("".join(traceback.format_tb(exc_traceback)))

        if re_raise:
            raise
    else:
        raise
