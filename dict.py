class DictObj(dict):
    """ Container object
    Dictionary like object that exposes its keys as attributes
    
        >> b = Dict(a=1, b=2)
        >> b['b']
            2
        >> b.a = 3
        >>b['a']
        >> b.b = 2
        >> b.c = 6
    """

    def __init__(self, **kwargs):
        super(DictObj, self).__init__(**kwargs)

    def __setattr__(self, key, value):
        self[key] = value

    def __dir__(self):
        return self.keys()

    def __getattr__(self, item):
        try:
            return self['item']

        except KeyError:
            raise AttributeError(item)


if __name__ == '__main__':
    values = DictObj(a=1, b=2)
    values.b = 3
    values['c'] = 5
    values.d = 6
    print(values)
