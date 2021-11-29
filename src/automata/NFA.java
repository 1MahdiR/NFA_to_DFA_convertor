package automata;

import java.util.ArrayList;
import java.util.HashMap;
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
                if (recursiveFunction(w, item))
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

    private List<State> unionStates(List<State> states, String w) {

        List<State> union = new ArrayList<>();
        for (State item:states) {

            union.addAll(nextState(item, w));
        }

        return union;
    }

    private State CreateNewState(List<State> states) {

        if (states.isEmpty())
            return new State("empty_state");

        String state_name = "";
        for (State item:states) {
            state_name += item.getName() + "_";
        }

        return new State(state_name.substring(0,state_name.length()-1));
    }

    public DFA convertToDFA(){

        Map<List<State>, Map<String, List<State>>> graph = new HashMap<>();

        List<State> q0_state = new ArrayList<>();
        q0_state.add(this.initialState);

        Map<String, List<State>> q0_edges = new HashMap<>();
        for (String w:this.alphabet) {
            q0_edges.put(w, nextState(q0_state.get(0), w));
        }

        graph.put(q0_state, q0_edges);

        boolean graphIsComplete = false;

        while (!graphIsComplete) {
            graphIsComplete = true;
            Map<List<State>, Map<String, List<State>>> temp_graph = new HashMap<>();
            for (List<State> item:graph.keySet()) {
                Map<String, List<State>> edges = graph.get(item);
                for (List<State> jtem:edges.values())
                    if (!graph.containsKey(jtem)) {
                        graphIsComplete = false;

                        Map<String, List<State>> current_edges = new HashMap<>();
                        for (String w:this.alphabet) {

                            current_edges.put(w, unionStates(jtem, w));
                        }

                        temp_graph.put(jtem, current_edges);
                    }
            }

            for (List<State> item:temp_graph.keySet()) {
                graph.put(item, temp_graph.get(item));
            }
        }

        Map<State, Map<String, State>> dfa_graph = new HashMap<>();
        List<State> finals = new ArrayList<>();
        Map<List<State>, State> mapper = new HashMap<>();

        for (List<State> item:graph.keySet()) {

            State st;
            if (!mapper.containsKey(item)) {

                st = CreateNewState(item);
                for (State cst:item) {
                    if (this.finalStates.contains(cst)) {
                        finals.add(st);
                        break;
                    }
                }
                mapper.put(item, st);
            } else {

                st = mapper.get(item);
                for (State cst:item) {
                    if (this.finalStates.contains(cst)) {
                        finals.add(st);
                        break;
                    }
                }
            }

            Map<String, State> edges = new HashMap<>();

            for (String w:graph.get(item).keySet()) {
                List<State> states = graph.get(item).get(w);
                if (!mapper.containsKey(states)) {
                    State new_st = CreateNewState(states);
                    mapper.put(states, new_st);
                    edges.put(w, new_st);
                } else {
                    edges.put(w, mapper.get(states));
                }
            }
            dfa_graph.put(st, edges);
        }

        State init_state = new State("");
        for(State item:dfa_graph.keySet()) {
            if (item.getName().equals(this.initialState.getName()))
                init_state = item;
        }

        return new DFA(this.name + "_(DFA)", this.alphabet, dfa_graph, init_state, finals);
    }

    @Override
    public String toString() {

        return String.format("NFA name: %s\n graph:\n %s\n initial state: %s\n final states:\n %s\n",
                this.name, this.graph, this.initialState, this.finalStates);
    }
}
