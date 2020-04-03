
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


def add_all(self):
    self.add_primitive("<", _less_than)
    self.add_primitive("<=", _less_equal)
    self.add_primitive(">", _larger_than)
    self.add_primitive(">=", _larger_equal)
    self.add_primitive("=", _equal)

    self.add_primitive("and", _and)
    self.add_primitive("or", _or)
    self.add_primitive("not", _not)
    