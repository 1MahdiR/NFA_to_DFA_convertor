package test;

import automata.DFA;
import automata.NFA;
import automata.State;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class test_11 {

    public static void main(String[] args) {

        State st0 = new State("q0");
        State st1 = new State("q1");
        State st2 = new State("q2");
        State st3 = new State("q3");
        State st4 = new State("q4");

        List<String> alphabet = new ArrayList<>();
        alphabet.add("0");
        alphabet.add("1");

        Map<State, Map<String, List<State>>> graph = new HashMap<>();
        Map<String, List<State>> q0_edges = new HashMap<>();
        Map<String, List<State>> q1_edges = new HashMap<>();
        Map<String, List<State>> q2_edges = new HashMap<>();
        Map<String, List<State>> q3_edges = new HashMap<>();
        Map<String, List<State>> q4_edges = new HashMap<>();

        List<State> q0_lambda_list = new ArrayList<>();
        q0_lambda_list.add(st1);
        q0_lambda_list.add(st3);
        q0_edges.put("lambda", q0_lambda_list);

        List<State> q1_0_list = new ArrayList<>();
        List<State> q1_1_list = new ArrayList<>();
        q1_0_list.add(st1);
        q1_1_list.add(st2);
        q1_edges.put("0", q1_0_list);
        q1_edges.put("1", q1_1_list);

        List<State> q2_0_list = new ArrayList<>();
        List<State> q2_1_list = new ArrayList<>();
        q2_0_list.add(st2);
        q2_1_list.add(st1);
        q2_edges.put("0", q2_0_list);
        q2_edges.put("1", q2_1_list);

        List<State> q3_0_list = new ArrayList<>();
        List<State> q3_1_list = new ArrayList<>();
        q3_0_list.add(st4);
        q3_1_list.add(st3);
        q3_edges.put("0", q3_0_list);
        q3_edges.put("1", q3_1_list);

        List<State> q4_0_list = new ArrayList<>();
        List<State> q4_1_list = new ArrayList<>();
        q4_0_list.add(st3);
        q4_1_list.add(st4);
        q4_edges.put("0", q4_0_list);
        q4_edges.put("1", q4_1_list);

        graph.put(st0, q0_edges);
        graph.put(st1, q1_edges);
        graph.put(st2, q2_edges);
        graph.put(st3, q3_edges);
        graph.put(st4, q4_edges);

        List<State> finals = new ArrayList<>();
        finals.add(st3);
        finals.add(st1);

        NFA my_nfa = new NFA("my_nfa", alphabet, graph, st0, finals);

        System.out.println(my_nfa);

        System.out.println("Converted to DFA:");
        DFA my_dfa = my_nfa.convertToDFA();
        System.out.println(my_dfa);

        System.out.println("does NFA accept '11011011'?");
        System.out.println(my_nfa.doesAcceptString("11011011"));
        System.out.println("does NFA accept '0110001000'?");
        System.out.println(my_nfa.doesAcceptString("0110001000"));
        System.out.println("does NFA accept '001111001001'?");
        System.out.println(my_nfa.doesAcceptString("001111001001"));

        System.out.println("does DFA accept '11011011'?");
        System.out.println(my_dfa.doesAcceptString("11011011"));
        System.out.println("does DFA accept '0110001000'?");
        System.out.println(my_dfa.doesAcceptString("0110001000"));
        System.out.println("does DFA accept '001111001001'?");
        System.out.println(my_dfa.doesAcceptString("001111001001"));
    }
}
