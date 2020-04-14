import string

_normal = "normal"
_string = "string"

def make_tokenizer(stream):

    def read_token():
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
                        return read_token()
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

    return read_token