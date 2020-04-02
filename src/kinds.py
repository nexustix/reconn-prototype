
_number = "number"
_string = "string"
_quote = "quote"


def as_number(token):
    try:
        return (True, int(token))
    except ValueError: pass;
    except TypeError: pass;
    return (None, None)

def as_string(token, remove_quotes):
    if type(token) == str and token.startswith('"') and token.endswith('"'):
        if remove_quotes:
            return (True, token[1:-1])
        else:
            return (True, token)
    return (None, None)

def as_quote(token, remove_quotes):
    if type(token) == str and token.startswith("'"):
        if remove_quotes:
            return (True, token[1:])
        else:
            return (True, token)
    return (None, None)


#HACK
def as_whatever(token, remove_quotes):
    success, v = as_number(token)
    if success:
        return _number, v
    
    success, v = as_string(token, remove_quotes)
    if success:
        return _string, v

    success, v = as_quote(token, remove_quotes)
    if success:
        return _quote, v
    
    return (None, token)