# A base class for all things which can have a name.
# The name is either empty or nonempty, but it is never
# NULL.
class Namable(object):

    def __init__(self):
        self.name = ''

    def set_name(self, name):
        self.name = name

    def clear_name(self):
        self.name = ''

    def has_name(self):
        return bool(self.name)

    def get_name(self):
        return self.name
