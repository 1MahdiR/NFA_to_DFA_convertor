
# automata language : (1((111)*+(000)*)1)+(0*(1+0))

from automata.state import State
from automata.nfa import NFA

name = "nfa_5"
comment = "(1((111)*+(000)*)1)+(0*(1+0))"
alphabet = ["0", "1"]
q0 = State("q0")
q1 = State("q1")
q2 = State("q2")
q3 = State("q3")
q4 = State("q4")
q5 = State("q5")
q6 = State("q6")
q7 = State("q7")
q8 = State("q8")
q9 = State("q9")
q10 = State("q10")
q11 = State("q11")
graph = { q0 : { "lambda" : [ q1 , q2 ] } , q1 : { "1" : [ q3 , q7 ] } , q3 : { "1" : [ q4 , q6 ] } , q4 : { "1" : [q5] } , q5 : { "1" : [q3] } ,
	q7 : { "1" : [q10] , "0" : [q8] } , q8 : { "0" : [q9] } , q9 : { "0" : [q7] }, q2 : { "0" : [ q2 , q11 ] , "1" : [q11] } }
initial = q0
finals = [q6, q10, q11]

nfa_5 = NFA(name, comment, alphabet, graph, initial, finals)

