
def _less_than(self):
    a = self.pop_value()
    b = self.pop_value()
    if b < a:
        self.push_value(1)
    else:
        self.push_value(0)


def _less_equal(self):
    a = self.pop_value()
    b = self.pop_value()
    if b <= a:
        self.push_value(1)
    else:
        self.push_value(0)


def _larger_than(self):
    a = self.pop_value()
    b = self.pop_value()
    if b > a:
        self.push_value(1)
    else:
        self.push_value(0)


def _larger_equal(self):
    a = self.pop_value()
    b = self.pop_value()
    if b >= a:
        self.push_value(1)
    else:
        self.push_value(0)


def _equal(self):
    a = self.pop_value()
    b = self.pop_value()
    if b == a:
        self.push_value(1)
    else:
        self.push_value(0)


def _and(self):
    a = self.pop_value()
    b = self.pop_value()
    if b and a:
        self.push_value(1)
    else:
        self.push_value(0)


def _or(self):
    a = self.pop_value()
    b = self.pop_value()
    if b or a:
        self.push_value(1)
    else:
        self.push_value(0)


def _not(self):
    a = self.pop_value()
    if a:
        self.push_value(0)
    else:
        self.push_value(1)

words = [
    [
        ("<", _less_than),
        ("<=", _less_equal),
        (">", _larger_than),
        (">=", _larger_equal),
        ("=", _equal),
        ("and", _and),
        ("or", _or),
        ("not", _not),
    ]]
    