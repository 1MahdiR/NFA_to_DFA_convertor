
# automata language : ((a+b)(a+b))*

from automata.state import State
from automata.dfa import DFA

name = "dfa_1"
alphabet = ["a", "b"]
q0 = State("q0")
q1 = State("q1")
graph = { q0 : { "a" : q1 , "b" : q1 }, q1 : { "a" : q0 , "b" : q0 } }
initial = q0
finals = [q0]

dfa_1 = DFA(name, alphabet, graph, initial, finals)

