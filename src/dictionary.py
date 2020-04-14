import util

class Dictionary():

    def __init__(self):
        self.words = {}

    def __getitem__(self, key):
        if type(key) == tuple:
            segs = key[0].split(".")
            head = key[1]
            
            if len(segs) > 0:
                for p in util.path_variants(segs):
                    tk = (p, head)
                    if tk in self.words:
                        return self.words[tk]
                if ("", head) in self.words:
                    return self.words["", head]
            else:
                return self.words["", head]
        else:
            raise Exception("need tuple as key")

    def __setitem__(self, key, value):
        if type(key) == tuple:
            self.words[key] = value
        else:
            raise Exception("need tuple as key")

    def __contains__(self, key):
        if type(key) == tuple:
            segs = key[0].split(".")
            head = key[1]
            
            if len(segs) > 0:
                for p in util.path_variants(segs):
                    tk = (p, head)
                    if tk in self.words:
                        return True
                if ("", head) in self.words:
                    return True
            elif ("", head) in self.words:
                return True
            return False
        else:
            raise Exception("need tuple as key")


if __name__ == "__main__":
    dict = Dictionary()
    dict["", "toaster"] = "foo"
    print(dict.words)
    #print(dict["best.path.ever", "toaster"])
    print(dict["best.path.ever", "toaster"])