
def _less_than(self):
    a = self.pop()
    b = self.pop()
    if b < a:
        self.push(1)
    else:
        self.push(0)


def _less_equal(self):
    a = self.pop()
    b = self.pop()
    if b <= a:
        self.push(1)
    else:
        self.push(0)


def _larger_than(self):
    a = self.pop()
    b = self.pop()
    if b > a:
        self.push(1)
    else:
        self.push(0)


def _larger_equal(self):
    a = self.pop()
    b = self.pop()
    if b >= a:
        self.push(1)
    else:
        self.push(0)


def _equal(self):
    a = self.pop()
    b = self.pop()
    if b == a:
        self.push(1)
    else:
        self.push(0)


def _and(self):
    a = self.pop()
    b = self.pop()
    if b and a:
        self.push(1)
    else:
        self.push(0)


def _or(self):
    a = self.pop()
    b = self.pop()
    if b or a:
        self.push(1)
    else:
        self.push(0)


def _not(self):
    a = self.pop()
    if a:
        self.push(0)
    else:
        self.push(1)


def add_all(self):
    self.add_word("<", _less_than)
    self.add_word("<=", _less_equal)
    self.add_word(">", _larger_than)
    self.add_word(">=", _larger_equal)
    self.add_word("=", _equal)

    self.add_word("and", _and)
    self.add_word("or", _or)
    self.add_word("not", _not)
    