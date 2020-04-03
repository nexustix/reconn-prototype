

def _add(self):
    a = self.pop_value()
    b = self.pop_value()
    self.push_value(b + a)


def _sub(self):
    a = self.pop_value()
    b = self.pop_value()
    self.push_value(b - a)


# def _div(self):
#     pass


def _mul(self):
    a = self.pop_value()
    b = self.pop_value()
    self.push_value(b * a)


def _mod(self):
    a = self.pop_value()
    b = self.pop_value()
    self.push_value(b % a)


def add_all(self):
    self.add_primitive("+", _add)
    self.add_primitive("-", _sub)
    self.add_primitive("*", _mul)
    self.add_primitive("%", _mod)
