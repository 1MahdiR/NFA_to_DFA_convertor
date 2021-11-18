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

    private boolean recursiveFunction(String w, State currentState) {

        if (w.isEmpty())
            return this.finalStates.contains(currentState);

        String target_edge = Character.toString(w.charAt(0));
        String restOf_w = w.substring(1);
        Map<String, List<State>> currentState_edges = this.graph.get(currentState);

        if (currentState_edges.containsKey(target_edge)) {

            List<State> possible_states = currentState_edges.get(target_edge);

            for (State item:possible_states) {
                if (recursiveFunction(restOf_w, item))
                    return true;
            }
        }
        else if (currentState_edges.containsKey("lambda")) {

            List<State> possible_states = currentState_edges.get("lambda");

            for (State item:possible_states) {
                if (recursiveFunction(restOf_w, item))
                    return true;
            }
        }

        return false;
    }

    public boolean doesAcceptString(String w) { return recursiveFunction(w, this.initialState); }

    @Override
    public String toString() {

        return String.format("NFA name: %s\n graph:\n %s\n initial state: %s\n final states:\n %s\n",
                this.name, this.graph, this.initialState, this.finalStates);
    }
}
