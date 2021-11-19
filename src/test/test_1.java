package test;

import automata.DFA;
import automata.State;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class test_1 {

    public static void main(String[] args){

        State st1 = new State("q0");
        State st2 = new State("q1");
        State st3 = new State("q2");
        System.out.println(st1);
        System.out.println(st2);
        System.out.println(st3);

        List<String> alphabet = new ArrayList<>();
        alphabet.add("a");

        Map<State, Map<String, State>> graph = new HashMap<>();
        Map<String, State> q0_edges = new HashMap<>();
        Map<String, State> q1_edges = new HashMap<>();
        Map<String, State> q2_edges = new HashMap<>();

        q0_edges.put("a", st2);
        q1_edges.put("a", st3);
        q2_edges.put("a", st3);

        graph.put(st1, q0_edges);
        graph.put(st2, q1_edges);
        graph.put(st3, q2_edges);

        List<State> finals = new ArrayList<>();
        finals.add(st3);
        finals.add(st1);

        System.out.println(graph);

        DFA my_dfa = new DFA("my_dfa", alphabet, graph, st1, finals);

        System.out.println(my_dfa);

        System.out.println("does accept ''?");
        System.out.println((my_dfa.doesAcceptString(""))); // true

        System.out.println("does accept 'a'?");
        System.out.println((my_dfa.doesAcceptString("a"))); // false

        System.out.println("does accept 'aa'?");
        System.out.println((my_dfa.doesAcceptString("aa"))); // true

        System.out.println("does accept 'aaa'?");
        System.out.println((my_dfa.doesAcceptString("aaa"))); // true

        System.out.println("does accept 'aaaa'?");
        System.out.println((my_dfa.doesAcceptString("aaaa"))); // true
    }
}
