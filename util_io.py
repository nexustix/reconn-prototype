import sys
import string

from recon import Recon


def _read_c(handle):
    return handle.read(1)

# def read_byte(lang: Recon):
#     lang.push_val(_read_b(sys.stdin))


def read_word(lang: Recon, handle=sys.stdin, encoding="utf-8"):
    c = _read_c(handle)
    n = 0
    while c not in string.whitespace:
        bs = bytes(c, encoding)
        for b in bs:
            lang.push_val(b)
            n += 1
        c = _read_c(handle)

    lang.push_val(n)


def print_val_pop(lang: Recon, handle=sys.stdout):
    handle.write(str(lang.pop_val())+"\n")
    handle.flush()
