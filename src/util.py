import sys

def warn(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)