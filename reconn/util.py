import sys

def warn(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def path_variants(segs, sep="."):
    r = []
    for n in range(len(segs), 0, -1):
        r.append(sep.join(segs[0:n]))
    return r