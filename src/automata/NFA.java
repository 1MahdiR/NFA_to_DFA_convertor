package automata;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;

public class NFA {

    private final String name;
    private final List<String> alphabet;
    private final Map<State, Map<String, List<State>>> graph;
    private final State initialState;
    private final List<State> finalStates;

    public NFA(String name, List<String> alphabet, Map<State, Map<String, List<State>>> graph, State initialState, List<State> finalStates) {
        this.name = name;
        this.alphabet = alphabet;
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

    public List<State> nextState(State st, String w) {
        List<State> states = new ArrayList<>();

        if (!w.isEmpty()) {
            if (this.graph.containsKey(st))
                if (this.graph.get(st).containsKey(w))
                    for (State item : this.graph.get(st).get(w)) {
                        states.add(item);
                        states.addAll(nextState(item, ""));
                    }
        }

        if (this.graph.containsKey(st))
            if (this.graph.get(st).containsKey("lambda"))
                for (State item:this.graph.get(st).get("lambda")) {
                    if (w.isEmpty())
                        states.add(item);
                    states.addAll(nextState(item, w));
                }

        return states;
    }

    private boolean isGraphComplete(Map<State, Map<String, List<State>>> graph) {

        for (State item:graph.keySet()) {
            Map<String, List<State>> edges = graph.get(item);
            if (edges.keySet().size() != this.alphabet.size())
                return false;
        }

        return true;
    }

    private List<State> unionStates(List<State> states, String w) {

        List<State> union = new ArrayList<>();
        for (State item:states) {

            union.addAll(nextState(item, w));
        }

        return union;
    }

    @Override
    public String toString() {

        return String.format("NFA name: %s\n graph:\n %s\n initial state: %s\n final states:\n %s\n",
                this.name, this.graph, this.initialState, this.finalStates);
    }
}
