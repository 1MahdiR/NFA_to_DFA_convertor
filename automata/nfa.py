
from automata.state import State
from automata.dfa import DFA

class NFA:

    def __init__(self, name:str, comment:str, alphabet:list,
            graph:dict, initialState:State, finalStates:list):

        self._name = name
        self._comment = comment # Comments could be used as a way to describe the language for convinience
        self._alphabet = frozenset(alphabet)
        self._graph = graph # graph = { node_1: { letter_1 : [ node_i, ...], ... }, ...  }
        self._initialState = initialState
        self._finalStates = frozenset(finalStates)

    def recursiveFunction(self, w:str, currentState:State) -> bool: # A secondary function which will be called by 'doesAcceptString()'

        if not w: # If the string is empty it means we iterated over string
            return currentState in self._finalStates # Returns true if current state is in final states

        target_edge = w[0] # The current letter that needs to be proccessed
        restOf_w = w[1:] # The rest of the string that needs to be iterated
        currentState_edges = self._graph[currentState] # Retrieve all edges from current state

        if target_edge in currentState_edges.keys():
            # There is at least one edge with letter 'target_edge'
            possible_states = currentState_edges[target_edge]

            for item in possible_states:
                if self.recursiveFunction(restOf_w, item): # For every state call this function recursively
                    return True

        if "lambda" in currentState_edges.keys(): # If there was no edge with letter 'target_edge',
            # find transitions with 'lambda'

            possible_states = currentState_edges["lambda"]

            for item in possible_states:
                if self.recursiveFunction(w, item): # For every state call this function recursively
                    return True

        return False

    def doesAcceptString(self, w:str) -> bool: # Calls a secondary function and returns true if nfa accepts the string
        return self.recursiveFunction(w, self._initialState)

    def nextState(self, st:State, w:str) -> frozenset: # Returns all possible states we can go from 'st' with string 'w'

        states = list()

        if w:
            if st in self._graph.keys():
                if w in self._graph[st].keys():
                    for item in self._graph[st][w]:
                        states.append(item)
                        for jtem in self.nextState(item, w[1:]): # Returns all possible states we can go from 'item' with string 'w[1:]'
                            states.append(jtem)

        if st in self._graph.keys(): # Same as previous nested ifs and fors, but changes state with lambda transition
            if "lambda" in self._graph[st].keys():
                for item in self._graph[st]["lambda"]:
                    if not w:
                        states.append(item)
                    for jtem in self.nextState(item, w):
                        states.append(jtem)

        return frozenset(states)

    def unionStates(self, states:frozenset, w:str) -> list: # Returns all states we can go from every state in 'states' with string 'w'

        union = list()
        for item in states:
            for jtem in self.nextState(item, w):
                union.append(jtem)

        return frozenset(union)

    def createNewState(self, states:frozenset): # Creates an union of states from the set'states'

        if not states: # If the set was empty return a new state 'empty_state'
            return State("empty_state")

        state_name = "_".join([ x.getName() for x in states ])

        return State(state_name)

    def convertToDFA(self):

        graph = dict() # Initiate graph

        q0_state = frozenset([self._initialState])
        q0_state = q0_state.union(self.nextState(self._initialState, "lambda")) # Get all transitions from 'q0' with 'lambda'

        q0_edges = dict()
        for i in self._alphabet:
            q0_edges[i] = self.unionStates(q0_state, i) # Find next states after 'q0_state' with letter 'i'

        graph[q0_state] = q0_edges # Assign q0_edges to graph
        q0_state_dfa = None

        graph_is_complete = False

        while not graph_is_complete: # If all nodes in graph had every edge with all letters in alphabet the algorithm is finished

            graph_is_complete = True # First we assume that graph IS complete
            temp_graph = dict()
            for item in graph.keys():
                edges = graph[item]

                for jtem in edges.values(): # Check every node that is connected to 'item'
                    if jtem not in graph: # If one node wan't defined in graph, the graph is NOT complete, so add that node and assign its edges
                        graph_is_complete = False

                        current_edges = dict()

                        for i in self._alphabet:
                            current_edges[i] = self.unionStates(jtem, i) # Just like 'q0_state'

                        temp_graph[jtem] = current_edges



            for item in temp_graph.keys(): # Transfer everything from temp_graph to graph
                graph[item] = temp_graph[item]

        dfa_graph = dict() # Initiate dfa graph
        finals = list()

        mapper = dict() # A dictionary to map list of states to single states ( { [q2,q1,q0]:q2_q1_q0, ... } )

        for item in graph.keys():
            if item not in mapper.keys(): # If this state wasn't in 'mapper'
                st = self.createNewState(item) # Create a new state from 'item'

                if item == q0_state: # If new state was the initial state
                    q0_state_dfa = st

                for jtem in item: # If at least one of the states in 'item' was a final state, add it to 'finals'
                    if jtem in self._finalStates:
                        finals.append(st)
                        break

                mapper[item] = st # Add this new state to 'mapper'

            else: # If this state was in 'mapper'

                st = mapper[item] # Retrieve the state from 'mapper'
                for jtem in item: # If at least one of the states in 'item' was a final state, add it to 'finals'
                    if jtem in self._finalStates:
                        finals.append(st)
                        break

            edges = dict() # Initiate edges for 'item' ( { letter_1 : [ node_i, ... ], ... } )

            for i in graph[item].keys():

                states = graph[item][i]
                if states not in mapper: # If this state wasn't in 'mapper'
                    new_st = self.createNewState(states) # Create a new state from 'states'
                    mapper[states] = new_st # Add this new state to 'mapper'
                    edges[i] = new_st # Add new edge with letter 'i'
                else: # If this state was in 'mapper'
                    edges[i] = mapper[states] # Retrieve edges from 'mapper'

            dfa_graph[st] = edges # Assign edges to state 'st'

        return DFA(self._name + "_(DFA)", self._comment, self._alphabet, dfa_graph, q0_state_dfa, frozenset(finals))

    def __str__(self): # A way to show the nfa for convinience

        return "NFA name: %s\n comment: %s\n graph:\n %s\n initial state: %s\n final states:\n %s\n" % (self._name, self._comment, self._graph, self._initialState, list(self._finalStates))

    def __repr__(self):

        return str(self)
