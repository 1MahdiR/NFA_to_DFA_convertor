
# automata language : (ab*a+ba*b)*

from automata.state import State
from automata.nfa import NFA

name = "nfa_3"
comment = "(ab*a+ba*b)*"
alphabet = ["a", "b"]
q0 = State("q0")
q1 = State("q1")
q2 = State("q2")
q3 = State("q3")
q4 = State("q4")
graph = { q0 : { "a" : [q3] , "b" : [q1] } , q1: { "a" : [q1] , "b" : [q2] } ,
        q2 : { "lambda" : [q0] } , q3 : { "a": [q4] , "b" : [q3] } , q4: { "lambda" : [q0] } }
initial = q0
finals = [q0]

nfa_3 = NFA(name, comment, alphabet, graph, initial, finals)

