

def _split(self):
    sep = self.pop_value()
    dat = self.pop_value()
    segs = dat.split(sep)
    for v in segs:
        self.push_value(v)
    self.push_value(len(segs))

def _nth(self):
    n = self.pop_value()
    dat = self.pop_value()
    self.push_value(dat[n])

def _concat(self):
    b = self.pop_value()
    a = self.pop_value()
    self.push_value(a+b)

"""
def _format(self):
    a = self.pop_value()
    values = []
    gapcount = a.count("{}")

    for n in range(gapcount):
        values.append(self.pop_value())
    
    self.push_value(a.format(*values))
"""

def _replace(self):
    marker = self.pop_value()
    insertable = self.pop_value()
    data = self.pop_value()
    r = data.replace(marker, insertable, 1)
    self.push_value(r)


words =[
    [
        ("split",_split),
        ("nth", _nth),
        ("concat", _concat),
        ("replace", _replace),
    ]]

# def add_all(self, prefix=""):
#     for w in words(prefix):
#         self.add_primitive(w[0], w[1])

