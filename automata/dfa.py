
from automata.state import State

class DFA:

    def __init__(self, name:str, comment:str, alphabet:list,
            graph:dict, initialState:State, finalStates:list):

        self._name = name
        self._comment = comment # Comments could be used as a way to describe the language for convinience
        self._alphabet = frozenset(alphabet)
        self._graph = graph
        self._finalStates = frozenset(finalStates)
        self._initialState = initialState

    def doesAcceptString(self, w:str) -> bool:

        currentState = self._initialState # Set initial state as current state
        for i in range(0, len(w)): # Iterates the string and for each letter it changes the state, based on "transition graph"
            target_edge = w[i]
            currentState_edges = self._graph[currentState]

            if target_edge in currentState_edges.keys():
                currentState = currentState_edges[target_edge]
            else:
                return False

        return currentState in self._finalStates  # returns true if the current state after iterating the string is one of the final states

    def __str__(self): # A way to show the dfa for convinience

        return "DFA name: %s\n comment: %s\n graph:\n %s\n initial state: %s\n final states:\n %s\n" % (self._name, self._comment, self._graph, self._initialState, list(self._finalStates))

    def __repr__(self):

        return str(self)
