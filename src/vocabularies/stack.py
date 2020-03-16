

def _swap(self):
    a = self.pop()
    b = self.pop()
    self.push(a)
    self.push(b)


def _drop(self):
    self.pop()


def _dup(self):
    a = self.pop()
    self.push(a)
    self.push(a)


def _over(self):
    a = self.pop()
    b = self.pop()
    self.push(b)
    self.push(a)
    self.push(b)


def _rot(self):
    a = self.pop()
    b = self.pop()
    c = self.pop()
    self.push(b)
    self.push(a)
    self.push(c)


def add_all(self):
    self.add_word("swap", _swap)
    self.add_word("drop", _drop)
    self.add_word("dup", _dup)
    self.add_word("over", _over)
    self.add_word("rot", _rot)
    