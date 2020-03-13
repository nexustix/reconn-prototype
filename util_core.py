import sys
import string

from recon import Recon


def _read_token(handle=sys.stdin, encoding="utf-8"):
    r = []
    c = handle.read(1)
    while c not in string.whitespace:
        bs = bytes(c, encoding)
        for b in bs:
            r.append(b)
        c = handle.read(1)

    return str(bytes(r), "utf-8")


def execute(lang: Recon, encoding="utf-8"):
    bs = []
    n = lang.pop_val()
    for i in range(n):
        bs.insert(0, lang.pop_val())

    word = str(bytes(bs), encoding)
    lang.execute(word)


def _as_number(token):
    try:
        return (True, int(token))
    except ValueError:
        return (None, None)


def interpret(lang: Recon, token):
    def ok():
        # sys.stdout.write("OK\n")
        pass
    if lang.execute(token):
        ok()
    else:
        result, number = _as_number(token)
        if not (result is None):
            lang.push_val(number)
            ok()
        else:
            sys.stdout.write("{} ?\n".format(token))


def interpret_loop(lang: Recon):
    while True:
        token = _read_token()
        if token != "bye":
            interpret(lang, token)
        else:
            break


def words(lang: Recon):
    prime = []
    common = []
    for k, v in lang.dict.items():
        kind, _ = v
        if kind == "prime":
            prime.append(k)
        elif kind == "common":
            common.append(k)
    for i in prime:
        sys.stdout.write(i+" ")
    sys.stdout.write("\n")
    for i in common:
        sys.stdout.write(i+" ")
    # sys.stdout.write("\n")
    sys.stdout.flush()
