
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

words = [
    [
        ("swap", _swap),
        ("drop", _drop),
        ("dup", _dup),
        ("over", _over),
        ("rot", _rot),
    ]]