package automata;

import java.util.Dictionary;

public class State {

    private final String name;
    private final Dictionary successors;
    private final boolean isFinal;
    private final boolean isInitial;

    public State(String name, Dictionary successors, boolean isFinal, boolean isInitial) {

        this.name = name;
        this.successors = successors;
        this.isFinal = isFinal;
        this.isInitial = isInitial;
    }

    @Override
    public String toString() {
        String final_state = "";
        String init_state = "";
        if (this.isInitial)
            init_state = "Initial";
        if (this.isFinal)
            final_state = "Final";

        return String.format("%s %s State %s : %s", final_state, init_state, this.name, this.successors);
    }
}
