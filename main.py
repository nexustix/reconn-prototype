import sys

from recon import Recon

import util_core
import util_io


recon = Recon()


def add(lang: Recon):
    a = lang.pop_val()
    b = lang.pop_val()
    lang.push_val(a + b)


def print_val_stack(lang: Recon):
    s = "<{}> ".format(len(recon.val_stack))
    for i in lang.val_stack:
        s += "{} ".format(i)
    s += "<- Top"
    sys.stdout.write(s+"\n")
    sys.stdout.flush()


def reverse(lang: Recon):
    bs = []
    n = lang.pop_val()
    for i in range(n):
        bs.insert(0, lang.pop_val())
    bs.reverse()
    for i in bs:
        lang.push_val(i)
    lang.push_val(n)


recon.register_primitive("+", lambda: add(recon))
recon.register_primitive("word<-", lambda: util_io.read_word(recon))
recon.register_primitive(".", lambda: util_io.print_val_pop(recon))
recon.register_primitive(".s", lambda: print_val_stack(recon))
recon.register_primitive("execute", lambda: util_core.execute(recon))
recon.register_primitive("words", lambda: util_core.words(recon))


print("<-> Welcome, execute \"bye\" to exit")

util_core.interpret_loop(recon)
recon.execute(".s")
