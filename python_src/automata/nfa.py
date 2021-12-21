
from automata.state import State
from automata.dfa import DFA

class NFA:

    def __init__(self, name:str, comment:str, alphabet:list,
            graph:dict, initialState:State, finalStates:list):

        self._name = name
        self._comment = comment
        self._alphabet = frozenset(alphabet)
        self._graph = graph
        self._initialState = initialState
        self._finalStates = frozenset(finalStates)

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

    def nextState(self, st:State, w:str) -> frozenset:

        states = list()

        if w:
            if st in self._graph.keys():
                if w in self._graph[st].keys():
                    for item in self._graph[st][w]:
                        states.append(item)
                        for jtem in self.nextState(item, w[1:]):
                            states.append(jtem)

        if st in self._graph.keys():
            if "lambda" in self._graph[st].keys():
                for item in self._graph[st]["lambda"]:
                    if not w:
                        states.append(item)
                    for jtem in self.nextState(item, w):
                        states.append(jtem)

        return frozenset(states)

    def unionStates(self, states:frozenset, w:str) -> list:

        union = list()
        for item in states:
            for jtem in self.nextState(item, w):
                union.append(jtem)

        return frozenset(union)

    def createNewState(self, states:frozenset):
        
        if not states:
            return State("empty_state")

        state_name = "_".join([ x.getName() for x in states ])
        
        return State(state_name)

    def convertToDFA(self):

        graph = dict()

        q0_state = frozenset([self._initialState])
        q0_state = q0_state.union(self.nextState(self._initialState, "lambda"))

        q0_edges = dict()
        for i in self._alphabet:
            q0_edges[i] = self.unionStates(q0_state, i)

        graph[q0_state] = q0_edges
        q0_state_dfa = None

        graph_is_complete = False

        while not graph_is_complete:

            graph_is_complete = True
            temp_graph = dict()
            for item in graph.keys():
                edges = graph[item]

                for jtem in edges.values():
                    if jtem not in graph:
                        graph_is_complete = False

                        current_edges = dict()

                        for i in self._alphabet:
                            current_edges[i] = self.unionStates(jtem, i)

                        temp_graph[jtem] = current_edges



            for item in temp_graph.keys():
                graph[item] = temp_graph[item]

        dfa_graph = dict()
        finals = list()

        mapper = dict()
    
        for item in graph.keys():
            if item not in mapper.keys():
                st = self.createNewState(item)

                if item == q0_state:
                    q0_state_dfa = st

                for jtem in item:
                    if jtem in self._finalStates:
                        finals.append(st)
                        break
                
                mapper[item] = st

            else:
                
                st = mapper[item]
                for jtem in item:
                    if jtem in self._finalStates:
                        finals.append(st)
                        break

            edges = dict()

            for i in graph[item].keys():

                states = graph[item][i]
                if states not in mapper:
                    new_st = self.createNewState(states)
                    mapper[states] = new_st
                    edges[i] = new_st
                else:
                    edges[i] = mapper[states]

            dfa_graph[st] = edges

        return DFA(self._name + "_(DFA)", self._alphabet, dfa_graph, q0_state_dfa, frozenset(finals))
    
    def __str__(self):

        return "DFA name: %s\n comment: %s\n graph:\n %s\n initial state: %s\n final states:\n %s\n" % (self._name, self._comment, self._graph, self._initialState, list(self._finalStates))

    def __repr__(self):

        return str(self)

