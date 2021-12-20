
from state import State

class DFA:

    def __init__(self, name:str, alphabet:list,
            graph:dict, initialState:State, finalStates:list):
        
        self._name = name
        self._alphabet = alphabet
        self._graph = graph
        self._finalStates = finalStates
        self._initialState = initialState

    def doesAcceptString(self, w:str) -> bool:

        currentState = self._initialState
        for i in range(0, len(w)):
            target_edge = w[i]
            currentState_edges = self._graph[currentState]

            if target_edge in currentState_edges.keys():
                currentState = currentState_edges[target_edge]
            else:
                return False

        return currentState in self._finalStates

    def __str__(self):

        return "DFA name: %s\n graph:\n %s\n initial state: %s\n final states:\n %s\n" % (self._name, self._graph, self._initialState, self._finalStates)

    def __repr__(self):

        return str(self)
