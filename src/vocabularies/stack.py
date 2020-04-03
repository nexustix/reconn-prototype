

def _swap(self):
    a = self.pop_value()
    b = self.pop_value()
    self.push_value(a)
    self.push_value(b)

def _drop(self):
    self.pop_value()


def _dup(self):
    a = self.pop_value()
    self.push_value(a)
    self.push_value(a)

def _over(self):
    a = self.pop_value()
    b = self.pop_value()
    self.push_value(b)
    self.push_value(a)
    self.push_value(b)

def _rot(self):
    a = self.pop_value()
    b = self.pop_value()
    c = self.pop_value()
    self.push_value(b)
    self.push_value(a)
    self.push_value(c)

def add_all(self):
    self.add_primitive("swap", _swap)
    self.add_primitive("drop", _drop)
    self.add_primitive("dup", _dup)
    self.add_primitive("over", _over)
    self.add_primitive("rot", _rot)
    