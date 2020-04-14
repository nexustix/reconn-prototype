

def _add(self):
    a = self.pop_value()
    b = self.pop_value()
    self.push_value(b + a)


def _sub(self):
    a = self.pop_value()
    b = self.pop_value()
    self.push_value(b - a)

def _mul(self):
    a = self.pop_value()
    b = self.pop_value()
    self.push_value(b * a)


def _mod(self):
    a = self.pop_value()
    b = self.pop_value()
    self.push_value(b % a)

words = [
    [
        ("+", _add),
        ("-", _sub),
        ("*", _mul),
        ("%", _mod),
    ]]
