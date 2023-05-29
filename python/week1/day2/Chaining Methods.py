class foo():
    def __init__(self, kind=None):
        self.kind = kind

    def __call__(self, kind=None):
        return foo(kind=kind)

    def my_print(self):
        print (self.kind)

    def line(self):
        return self(kind='line')
    def bar(self):
        return self(kind='bar')