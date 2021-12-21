
# # # # # # # # # # # # # # # # # # # #
# NFA to DFA convertor                #
# author: __ray__                     #
# email: a.m.rasouli.n@gmail.com      #
# github: https://github.com/1MahdiR  #
# # # # # # # # # # # # # # # # # # # #

from automata.dfa import DFA
from automata.nfa import NFA

AUTOS = list()

def select_automata(automata):

    dfa_or_nfa = "DFA" if type(automata) == DFA else "NFA"
    print("\n        Automata ({})".format(dfa_or_nfa))
    print("------------------------------")
    print("Automata name: {}".format(automata._name))
    print("1. Enter a string")
    print("2. Show definition of automata")
    print("3. Show visualization of automata")
    if dfa_or_nfa == "NFA":
        print("4. Convert to DFA")
        print("5. Delete automata")
        print("6. Exit\n")
    else:
        print("4. Delete automata")
        print("5. Exit\n")

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
            pass

        elif reply == "4":
            if type(automata) == DFA:
                AUTOS.remove(automata)
                return None
            else:
                dfa = automata.convertToDFA()
                AUTOS.append(dfa)
                print("\nAutomata {} has been created\n".format(dfa._name))

        elif reply == "5":
            if type(automata) == DFA:
                return None
            else:
                AUTOS.remove(automata)
                return None
        elif reply == "6":
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

    while True:

        main_menu()
        reply = input("> ")
        if reply in valid_inputs:
            if reply == "1":
                pass
            elif reply == "2":
                pass
            elif reply == "3":
                load_automata()
            elif reply == "4":
                load_prefabs()
            else:
                break
        else:
            pass


if __name__ == '__main__':
    main()

