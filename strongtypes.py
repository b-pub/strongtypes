#
# Python function prototype decorator
#
# Copyright 2018 Brent Burton
#
# This code is licensed under the MIT license.
# See file LICENSE for details.
#

# A decorator to check args. @prototype(type,type,...)
def prototype(*protoargs):
    def prototype_decorator(func):
        def _wrap(*args):
            # Confirm argument counts match
            if len(protoargs) < len(args):
                raise TypeError, "Too many parameters to %s. Expected %d" % (func.__name__, len(protoargs))
            if len(protoargs) > len(args):
                raise TypeError, "Not enough parameters to %s. Expected %d" % (func.__name__, len(protoargs))
            # Compare corresponding entries in types and args
            for i in xrange(len(protoargs)):
                if not isinstance(args[i], protoargs[i]):
                    raise TypeError, "Argument %d of %s is invalid type, expected %s" % (i, func.__name__, str(protoargs[i]))
            # Everything checks out, call the function
            func(*args)
        return _wrap
    return prototype_decorator
