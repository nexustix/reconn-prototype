import string

_normal = "normal"
_string = "string"

def read_token(stream):
    s = ''
    v = stream.read(1)
    mode = _normal
    n = 0

    if v == '"':
        mode = _string
        s += v

    while v:
        if mode == _normal:
            if v in string.whitespace:
                if not n:
                    return read_token(stream)
                else:
                    break
            s += v
        elif mode == _string and n:
            if v == '"':
                if not stream.read(1) == '"':
                    s += '"'
                    break
            s += v

        n += 1
        v = stream.read(1)

    return (n, s)


if __name__ == "__main__":

    print(string.whitespace)
    stream = open("test.rcn", "r")


    for i in range(10):
        cake = read_token(stream)
        print(cake)