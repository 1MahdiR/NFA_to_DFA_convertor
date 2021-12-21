
class State:

    def __init__(self, name:str):
        self._name = name

    def getName(self) -> str:
        return self._name

    def __str__(self):
        return "State %s" % self.getName()
    
    def __repr__(self):
        return str(self)

