def forceType(obj, typ):
    if not isinstance(obj, typ):
        s = str(type(obj)) + " was not of type " + str(type(typ))
        raise TypeError(s)
    return obj
