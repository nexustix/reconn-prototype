

def _add(self):
    a = self.pop()
    b = self.pop()
    self.push(b + a)


def _sub(self):
    a = self.pop()
    b = self.pop()
    self.push(b - a)


# def _div(selfe):
#     pass


def _mul(self):
    a = self.pop()
    b = self.pop()
    self.push(b * a)


def _mod(self):
    a = self.pop()
    b = self.pop()
    self.push(b % a)


def add_all(self):
    self.add_word("+", _add)
    self.add_word("-", _sub)
    self.add_word("*", _mul)
    self.add_word("%", _mod)
