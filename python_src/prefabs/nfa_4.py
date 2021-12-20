
# automata language : 0*(0+1)

from automata.state import State
from automata.nfa import NFA

name = "nfa_3"
alphabet = ["0", "1"]
q0 = State("q0")
q1 = State("q1")
q2 = State("q2")
graph = { q0 : { "0" : [q0, q1] , "1" : [q1] } , q1: { "0" : [q2] , "1" : [q2] } ,
        q2 : { "1" : [q2] } }
initial = q0
finals = [q1]

nfa_4 = NFA(name, alphabet, graph, initial, finals)

