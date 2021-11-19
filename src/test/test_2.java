package test;

import automata.NFA;
import automata.State;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class test_2 {

    public static void main(String[] args) {

        State st0 = new State("q0");
        State st1 = new State("q1");
        State st2 = new State("q2");
        State st3 = new State("q3");
        State st4 = new State("q4");
        State st5 = new State("q5");

        List<String> alphabet = new ArrayList<>();
        alphabet.add("a");
        alphabet.add("b");

        Map<State, Map<String, List<State>>> graph = new HashMap<>();
        Map<String, List<State>> q0_edges = new HashMap<>();
        Map<String, List<State>> q1_edges = new HashMap<>();
        Map<String, List<State>> q2_edges = new HashMap<>();
        Map<String, List<State>> q3_edges = new HashMap<>();
        Map<String, List<State>> q4_edges = new HashMap<>();
        Map<String, List<State>> q5_edges = new HashMap<>();

        List<State> q0_a_list = new ArrayList<>();
        q0_a_list.add(st1);
        q0_edges.put("a", q0_a_list);

        List<State> q1_a_list = new ArrayList<>();
        q1_a_list.add(st2);
        q1_a_list.add(st4);
        q1_edges.put("a", q1_a_list);

        List<State> q2_b_list = new ArrayList<>();
        q2_b_list.add(st3);
        q2_edges.put("b", q2_b_list);

        List<State> q4_a_list = new ArrayList<>();
        q4_a_list.add(st5);
        q4_edges.put("a", q4_a_list);

        graph.put(st0, q0_edges);
        graph.put(st1, q1_edges);
        graph.put(st2, q2_edges);
        graph.put(st3, q3_edges);
        graph.put(st4, q4_edges);
        graph.put(st5, q5_edges);

        System.out.println(graph);

        List<State> finals = new ArrayList<>();
        finals.add(st3);
        finals.add(st5);

        NFA my_nfa = new NFA("my_nfa", alphabet, graph, st0, finals);

        System.out.println();
        System.out.println(my_nfa);
    }
}
