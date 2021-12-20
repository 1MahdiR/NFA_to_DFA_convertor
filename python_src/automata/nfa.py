
from automata.state import State
from automata.dfa import DFA

class NFA:

    def __init__(self, name:str, alphabet:list,
            graph:dict, initialState:State, finalStates:list):

        self._name = name
        self._alphabet = alphabet
        self._graph = graph
        self._initialState = initialState
        self._finalStates = finalStates

    def recursiveFunction(self, w:str, currentState:State) -> bool:
        
        if not w:
            return currentState in self._finalStates

        target_edge = w[0]
        restOf_w = w[1:]
        currentState_edges = self._graph[currentState]

        if target_edge in currentState_edges.keys():

            possible_states = currentState_edges[target_edge]

            for item in possible_states:
                if self.recursiveFunction(restOf_w, item):
                    return True

        elif "lambda" in currentState_edges.keys():

            possible_states = currentState_edges["lambda"]

            for item in possible_states:
                if self.recursiveFunction(w, item):
                    return True

        return False

    def doesAcceptString(self, w:str) -> bool:
        return self.recursiveFunction(w, self._initialState)


