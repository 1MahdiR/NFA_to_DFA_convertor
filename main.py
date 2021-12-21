
# # # # # # # # # # # # # # # # # # # #
# NFA to DFA convertor                #
# author: __ray__                     #
# email: a.m.rasouli.n@gmail.com      #
# github: https://github.com/1MahdiR  #
# # # # # # # # # # # # # # # # # # # #

from automata.dfa import DFA
from automata.nfa import NFA
from automata.state import State

AUTOS = list()

def create_new_dfa():
    name = ""
    comment = ""
    alphabet = list()
    graph = dict()
    initial = None
    finals = list()
    states = dict()

    print("Enter the name of the dfa.")
    while True:
        reply = input("> ")
        if reply.strip():
            name = reply
            break

    print("Enter a comment for dfa (optional).")
    comment = input("> ").strip()

    print("Enter the alphabet of the dfa (seperate with spaces).")
    while True:
        reply = input("> ").strip().split()
        alphabet = [ x for x in reply if x ]
        if alphabet:
            break
        print("Error in input!")
    
    print("Enter the graph definition of the dfa ([source:w:destination]).")
    while True:
        reply = input("> ")
        if not reply and graph:
            break
        reply = reply.strip().split(":")
        if len(reply) == 3 and all(reply) and len(reply[1]) == 1:
            w = reply[1]
            if w not in alphabet:
                print("Error in input!")
                continue
            q1 = reply[0]
            q2 = reply[2]

            q1_state = None
            q2_state = None

            if not states.get(q1):
                q1_state = State(q1)
                states[q1] = q1_state
            else:
                q1_state = states[q1]

            if not states.get(q2):
                q2_state = State(q2)
                states[q2] = q2_state
            else:
                q2_state = states[q2]

            if graph.get(q1_state):
                graph[q1_state][w] = q2_state
            else:
                graph[q1_state] = dict()
                graph[q1_state][w] = q2_state
    
    print("What is the initial state of dfa?")
    while True:
        reply = input("> ").strip()
        if states.get(reply):
            initial = states[reply]
            break

    print("What are the final states of dfa (seperate with spaces)?")
    while True:
        reply = input("> ").strip().split()

        for item in reply:
            if states.get(item):
                finals.append(states[item])
            else:
                continue
        break

    dfa = DFA(name, comment, alphabet, graph, initial, finals)
    AUTOS.append(dfa)

    print("dfa {} has been successfully created.".format(dfa._name))

def create_new_nfa():
    name = ""
    comment = ""
    alphabet = list()
    graph = dict()
    initial = None
    finals = list()
    states = dict()

    print("Enter the name of the nfa.")
    while True:
        reply = input("> ")
        if reply.strip():
            name = reply
            break

    print("Enter a comment for nfa (optional).")
    comment = input("> ").strip()

    print("Enter the alphabet of the nfa (seperate with spaces).")
    while True:
        reply = input("> ").strip().split()
        alphabet = [ x for x in reply if x ]
        if alphabet:
            break
        print("Error in input!")
    
    print("Enter the graph definition of the nfa ([source:w:destination]).")
    while True:
        reply = input("> ")
        if not reply and graph:
            break
        reply = reply.strip().split(":")
        if len(reply) == 3 and all(reply) and (len(reply[1]) == 1 or reply[1] == "lambda"):
            w = reply[1].strip()
            if w not in alphabet and  w != "lambda":
                print("Error in input!")
                continue
            q1 = reply[0]
            q2 = reply[2]

            q1_state = None
            q2_state = None

            if not states.get(q1):
                q1_state = State(q1)
                states[q1] = q1_state
            else:
                q1_state = states[q1]

            if not states.get(q2):
                q2_state = State(q2)
                states[q2] = q2_state
            else:
                q2_state = states[q2]

            if graph.get(q1_state):
                if graph[q1_state].get(w):
                    if q2_state not in graph[q1_state][w]:
                        graph[q1_state][w].append(q2_state)
                else:
                    graph[q1_state][w] = [q2_state]
            else:
                graph[q1_state] = dict()
                graph[q1_state][w] = [q2_state]
    
    print("What is the initial state of nfa?")
    while True:
        reply = input("> ").strip()
        if states.get(reply):
            initial = states[reply]
            break

    print("What are the final states of nfa (seperate with spaces)?")
    while True:
        reply = input("> ").strip().split()

        for item in reply:
            if states.get(item):
                finals.append(states[item])
            else:
                continue
        break

    nfa = NFA(name, comment, alphabet, graph, initial, finals)
    AUTOS.append(nfa)

    print("nfa {} has been successfully created.".format(nfa._name))

def select_automata(automata):

    dfa_or_nfa = "DFA" if type(automata) == DFA else "NFA"
    print("\n        Automata ({})".format(dfa_or_nfa))
    print("------------------------------")
    print("Automata name: {}".format(automata._name))
    print("1. Enter a string")
    print("2. Show definition of automata")
    if dfa_or_nfa == "NFA":
        print("3. Convert to DFA")
        print("4. Delete automata")
        print("5. Exit\n")
    else:
        print("3. Delete automata")
def select_automata(automata):

    dfa_or_nfa = "DFA" if type(automata) == DFA else "NFA"
    print("\n        Automata ({})".format(dfa_or_nfa))
    print("------------------------------")
    print("Automata name: {}".format(automata._name))
    print("1. Enter a string")
    print("2. Show definition of automata")
    if dfa_or_nfa == "NFA":
        print("3. Convert to DFA")
        print("4. Delete automata")
        print("5. Exit\n")
    else:
        print("3. Delete automata")
        print("4. Exit\n")

    while True:
        reply = input("> ")
        if reply == "1":
            string = input("Enter a strnig as input: ")
            if automata.doesAcceptString(string):
                print("'{}' is accepted by the automata.".format(string))
            else:
                print("'{}' is NOT accepted by the automata.".format(string))
        elif reply == "2":
            print()
            print(automata)
            print()

        elif reply == "3":
            if type(automata) == DFA:
                AUTOS.remove(automata)
                return None
            else:
                dfa = automata.convertToDFA()
                AUTOS.append(dfa)
                print("\nAutomata {} has been created\n".format(dfa._name))

        elif reply == "4":
            if type(automata) == DFA:
                return None
            else:
                AUTOS.remove(automata)
                return None
        elif reply == "5":
            if type(automata) != DFA:
                return None



def load_automata_menu():

    print("\n       Load an automata")
    print("------------------------------")

    if AUTOS:
        for index, item in enumerate(AUTOS):
            dfa_or_nfa = "DFA" if type(item) == DFA else "NFA"
            print(" {:<4}{:.<20}{}".format(index+1, item._name, dfa_or_nfa))
        print()
    else:
        print(" There is no automata to load!")


def load_automata():
    
    load_automata_menu()
    valid_inputs = list(range(1, len(AUTOS)+1))
    reply = input("> ")
    if reply.isdigit() and int(reply) in valid_inputs:
        select_automata(AUTOS[int(reply)-1])

def load_prefabs():
    try:
        from prefabs.nfa_1 import nfa_1
        from prefabs.nfa_2 import nfa_2
        from prefabs.nfa_3 import nfa_3
        from prefabs.nfa_4 import nfa_4
        from prefabs.nfa_5 import nfa_5
        from prefabs.dfa_1 import dfa_1
        
        if dfa_1 not in AUTOS:
            AUTOS.append(dfa_1)
        if nfa_1 not in AUTOS:
            AUTOS.append(nfa_1)
        if nfa_2 not in AUTOS:
            AUTOS.append(nfa_2)
        if nfa_3 not in AUTOS:
            AUTOS.append(nfa_3)
        if nfa_4 not in AUTOS:
            AUTOS.append(nfa_4)
        if nfa_5 not in AUTOS:
            AUTOS.append(nfa_5)

        print("\nAutomatas are loaded successfully!\n")

    except ImportError:
        print("\nSorry! no prefabs are found.\n")

def main_menu():
    
    st = """
   nfa_to_dfa_convertor
--------------------------
1. Create a new DFA
2. Create a new NFA
3. Load an automata
4. Load from prefabs
5. Exit
"""

    print(st)

def main():
    
    valid_inputs = ["1", "2", "3", "4", "5"]

    try:
        while True:

            main_menu()
            reply = input("> ")
            if reply in valid_inputs:
                if reply == "1":
                    create_new_dfa()
                elif reply == "2":
                    create_new_nfa()
                elif reply == "3":
                    load_automata()
                elif reply == "4":
                    load_prefabs()
                else:
                    break
            else:
                pass
    
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()

