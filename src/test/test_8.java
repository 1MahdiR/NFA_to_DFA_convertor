package test;

import automata.NFA;
import automata.State;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class test_8 {

    public static void main(String[] args) {

        State st0 = new State("q0");
        State st1 = new State("q1");
        State st2 = new State("q2");
        State st3 = new State("q3");
        State st4 = new State("q4");
        State st5 = new State("q5");
        State st6 = new State("q6");
        State st7 = new State("q7");

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
        Map<String, List<State>> q6_edges = new HashMap<>();
        Map<String, List<State>> q7_edges = new HashMap<>();

        List<State> q0_b_list = new ArrayList<>();
        List<State> q0_lambda_list = new ArrayList<>();
        q0_b_list.add(st1);
        q0_b_list.add(st2);
        q0_lambda_list.add(st5);
        q0_edges.put("b", q0_b_list);
        q0_edges.put("lambda", q0_lambda_list);

        List<State> q2_a_list = new ArrayList<>();
        List<State> q2_lambda_list = new ArrayList<>();
        q2_a_list.add(st3);
        q2_lambda_list.add(st4);
        q2_edges.put("a", q2_a_list);
        q2_edges.put("lambda", q2_lambda_list);

        List<State> q4_a_list = new ArrayList<>();
        List<State> q4_lambda_list = new ArrayList<>();
        q4_a_list.add(st7);
        q4_lambda_list.add(st6);
        q4_edges.put("a", q4_a_list);
        q4_edges.put("lambda", q4_lambda_list);

        graph.put(st0, q0_edges);
        graph.put(st1, q1_edges);
        graph.put(st2, q2_edges);
        graph.put(st3, q3_edges);
        graph.put(st4, q4_edges);
        graph.put(st5, q5_edges);
        graph.put(st6, q6_edges);
        graph.put(st7, q7_edges);

        List<State> finals = new ArrayList<>();
        finals.add(st3);
        finals.add(st6);
        finals.add(st7);

        NFA my_nfa = new NFA("my_nfa", alphabet, graph, st0, finals);

        System.out.println(my_nfa);

        System.out.println();

        System.out.println(my_nfa.nextState(st0,"b"));
        System.out.println(my_nfa.nextState(st0,""));
        System.out.println(my_nfa.nextState(st2, "a"));
    }
}
