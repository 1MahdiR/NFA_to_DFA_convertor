package automata;

public class State {

    private final String name;

    public State(String name) { this.name = name; }

    public String getName() {
        return name;
    }

    @Override
    public String toString() {

        return String.format("State %s", this.name);
    }
}
