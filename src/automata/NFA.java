package automata;

import java.util.List;
import java.util.Map;

public class NFA {

    private final String name;
    private final Map<State, Map<String, List<State>>> graph;
    private final State initialState;
    private final List<State> finalStates;

    public NFA(String name, Map<State, Map<String, List<State>>> graph, State initialState, List<State> finalStates) {
        this.name = name;
        this.graph = graph;
        this.finalStates = finalStates;
        this.initialState = initialState;
    }

    @Override
    public String toString() {

        return String.format("NFA name: %s\n graph:\n %s\n initial state: %s\n final states:\n %s\n",
                this.name, this.graph, this.initialState, this.finalStates);
    }
}
