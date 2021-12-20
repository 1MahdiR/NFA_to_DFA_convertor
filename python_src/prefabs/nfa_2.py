	
# automata language : (aaa+bbb)*

from automata.state import State
from automata.nfa import NFA

name = "nfa_2"
alphabet = ["a", "b"]
q0 = State("q0")
q1 = State("q1")
q2 = State("q2")
q3 = State("q3")
q4 = State("q4")
graph = { q0 : { "a" : [q1] , "b" : [q3] }, q1: { "a": [q2] },
        q2 : { "a" : [q0] }, q3 : { "b" : [q4] }, q4 : { "b" : [q0] } }
initial = q0
finals = [q0]

nfa_2 = NFA(name, alphabet, graph, initial, finals)

