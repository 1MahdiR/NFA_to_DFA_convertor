package test;

import automata.NFA;
import automata.State;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class test_5 {

    public static void main(String[] args) {

        State st0 = new State("q0");
        State st1 = new State("q1");
        State st2 = new State("q2");

        Map<State, Map<String, List<State>>> graph = new HashMap<>();
        Map<String, List<State>> q0_edges = new HashMap<>();
        Map<String, List<State>> q1_edges = new HashMap<>();
        Map<String, List<State>> q2_edges = new HashMap<>();

        List<State> q0_0_list = new ArrayList<>();
        List<State> q0_1_list = new ArrayList<>();
        q0_0_list.add(st1);
        q0_1_list.add(st1);
        q0_edges.put("0", q0_0_list);
        q0_edges.put("1", q0_1_list);

        List<State> q1_0_list = new ArrayList<>();
        List<State> q1_1_list = new ArrayList<>();
        List<State> q1_lambda_list = new ArrayList<>();
        q1_0_list.add(st2);
        q1_0_list.add(st0);
        q1_1_list.add(st1);
        q1_lambda_list.add(st2);
        q1_edges.put("0", q1_0_list);
        q1_edges.put("1", q1_1_list);
        q1_edges.put("lambda", q1_lambda_list);

        List<State> q2_1_list = new ArrayList<>();
        q2_1_list.add(st1);
        q2_edges.put("1", q2_1_list);

        graph.put(st0, q0_edges);
        graph.put(st1, q1_edges);
        graph.put(st2, q2_edges);

        List<State> finals = new ArrayList<>();
        finals.add(st1);

        NFA my_nfa = new NFA("my_nfa", graph, st0, finals);

        System.out.println("does accept ''?");
        System.out.println(my_nfa.doesAcceptString("")); // false

        System.out.println("does accept '00'?");
        System.out.println(my_nfa.doesAcceptString("00")); // false

        System.out.println("does accept '10010'?");
        System.out.println(my_nfa.doesAcceptString("10010")); // false

        System.out.println("does accept '01001'?");
        System.out.println(my_nfa.doesAcceptString("01001")); // true

        System.out.println("does accept '0000'?");
        System.out.println(my_nfa.doesAcceptString("0000")); // false

        System.out.println("does accept '000'?");
        System.out.println(my_nfa.doesAcceptString("000")); // true
    }
}
