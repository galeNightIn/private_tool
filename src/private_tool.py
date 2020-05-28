__all__ = ['un_private_class']


def un_private_class(cls: type = None):
    """ Return the same class as was wrapped in with changed
    __getattr__ method to get access for private attributes

    Usage:
            @un_private_class
            class A:
                ...
        or
            A = un_private_class(A)
    """
    def getattribute_w(self: object, name: str):
        if name.startswith("__") and not name.endswith("__"):
            name = "_%s%s" % (cls.__name__, name)
        return self.__getattribute__(name)

    cls.__getattr__ = getattribute_w

    return cls
