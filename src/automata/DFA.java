package automata;

import java.util.List;
import java.util.Map;

public class DFA {

    private final String name;
    private final List<String> alphabet;
    private final Map<State, Map<String, State>> graph;
    private final State initialState;
    private final List<State> finalStates;

    public DFA(String name, List<String> alphabet, Map<State, Map<String, State>> graph, State initialState, List<State> finalStates) {
        this.name = name;
        this.alphabet = alphabet;
        this.graph = graph;
        this.finalStates = finalStates;
        this.initialState = initialState;
    }

    public boolean doesAcceptString(String w) {

        State currentState = this.initialState;
        for (int i = 0; i < w.length(); i++)
        {
            String target_edge = Character.toString(w.charAt(i));
            Map<String, State> currentState_edges = this.graph.get(currentState);

            if (currentState_edges.containsKey(target_edge))
                currentState = currentState_edges.get(target_edge);
            else
                return false;
        }

        return this.finalStates.contains(currentState);
    }

    @Override
    public String toString() {

        return String.format("DFA name: %s\n graph:\n %s\n initial state: %s\n final states:\n %s\n",
                this.name, this.graph, this.initialState, this.finalStates);
    }

}
