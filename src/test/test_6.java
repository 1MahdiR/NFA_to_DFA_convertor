package test;

import automata.NFA;
import automata.State;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class test_6 {

    public static void main(String[] args) {

        State st0 = new State("q0");
        State st1 = new State("q1");
        State st2 = new State("q2");

        List<String> alphabet = new ArrayList<>();
        alphabet.add("a");
        alphabet.add("b");

        Map<State, Map<String, List<State>>> graph = new HashMap<>();
        Map<String, List<State>> q0_edges = new HashMap<>();
        Map<String, List<State>> q1_edges = new HashMap<>();
        Map<String, List<State>> q2_edges = new HashMap<>();

        List<State> q0_a_list = new ArrayList<>();
        List<State> q0_lambda_list = new ArrayList<>();
        q0_a_list.add(st2);
        q0_lambda_list.add(st1);
        q0_edges.put("a", q0_a_list);
        q0_edges.put("lambda", q0_lambda_list);

        List<State> q1_b_list = new ArrayList<>();
        List<State> q1_lambda_list = new ArrayList<>();
        q1_b_list.add(st1);
        q1_lambda_list.add(st2);
        q1_edges.put("b", q1_b_list);
        q1_edges.put("lambda", q1_lambda_list);

        List<State> q2_a_list = new ArrayList<>();
        q2_a_list.add(st2);
        q2_edges.put("a", q2_a_list);

        graph.put(st0, q0_edges);
        graph.put(st1, q1_edges);
        graph.put(st2, q2_edges);

        List<State> finals = new ArrayList<>();
        finals.add(st1);
        finals.add(st2);

        NFA my_nfa = new NFA("my_nfa", alphabet, graph, st0, finals);

        System.out.println("does accept ''?");
        System.out.println(my_nfa.doesAcceptString("")); // false

        System.out.println("does accept 'bb'?");
        System.out.println(my_nfa.doesAcceptString("bb")); // true

        System.out.println("does accept 'bbaabb'?");
        System.out.println(my_nfa.doesAcceptString("bbaabb")); // false

        System.out.println("does accept 'aaaaaa'?");
        System.out.println(my_nfa.doesAcceptString("aaaaaa")); // true

        System.out.println("does accept 'aaaaaab'?");
        System.out.println(my_nfa.doesAcceptString("aaaaaab")); // false

        System.out.println("does accept 'baaaa'?");
        System.out.println(my_nfa.doesAcceptString("baaaa")); // true
    }
}
