import sys

_prime = "prime"
_common = "common"


def tg(c, k, d=None):
    try:
        return c[k]
    except:
        return d


class Recon():

    def __init__(self):
        self.val_stack = []
        self.run_stack = []
        self.dict = {}

    def push_val(self, val):
        self.val_stack.append(val)

    def pop_val(self):
        return self.val_stack.pop()

    def push_run(self, val):
        self.run_stack.append(val)

    def pop_run(self):
        return self.val_stack.pop()

    def register_primitive(self, name, function):
        self.dict[name] = (_prime, function)

    def register_derivative(self, name, words):
        self.dict[name] = (_common, words)

    def get_word(self, name):
        return self.dict[name]

    def _run(self):
        while len(self.run_stack) > 0:
            self.run_stack.pop()()

    def execute(self, word):
        kind, data = tg(self.dict, word, (None, None))
        if kind:
            if kind == _prime:
                self.push_run(data)
            elif kind == _common:
                for w in data:
                    self.execute(w)
        else:
            # print("{} ?".format(word))
            self.run_stack = []
            return False

        try:
            self._run()
        except Exception as e:
            sys.stdout.write("{} !\n".format(e))
            sys.stdout.flush()
        return True
