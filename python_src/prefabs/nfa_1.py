
# automata language : (aa)+(bb*)

from automata.state import State
from automata.nfa import NFA

name = "nfa_1"
alphabet = ["a", "b"]
q0 = State("q0")
q1 = State("q1")
q2 = State("q2")
q3 = State("q3")
graph = { q0 : { "a" : [q1] , "b" : [q2] }, q1: { "a": [q3] },
        q2 : { "b" : [q2, q3], "lambda" : [q3] }, q3 : {} }
initial = q0
finals = [q3]

nfa_1 = NFA(name, alphabet, graph, initial, finals)

