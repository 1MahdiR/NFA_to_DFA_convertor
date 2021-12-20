
class State:

    def __init__(self, name:str):
        self._name = name

    def getName(self):
        return self._name

    def __str__(self):
        return "State %s" % self.getName()

