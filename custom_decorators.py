from __future__ import unicode_literals

from functools import wraps

import sys
import traceback

def print_errors(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except:
            etype, value, tb = sys.exc_info()
            print "caught an error :(", value, etype
            print ''.join(traceback.format_exception(etype, value, tb))
            raise
    return wrapper

