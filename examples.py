# Example Turing Machine object from "Destroy all Software" screencast (modified to fit our format)

X_B_TRANSITION_FUNC = {
    ("s1", "B"): ("s2", "X", "R"),
    ("s2", "B"): ("s3", "B", "L"),
    ("s3", "X"): ("s4", "B", "R"),
    ("s4", "B"): ("s1", "B", "L"),
}

t = TuringMachine(
    states={"s1", "s2", "s3", "s4", "s5"},
    alphabet={"B", "X"},
    blank_symbol="B",
    initial_tape=["B", "B"],
    initial_state="s1",
    final_states={"s5"},
    transition_func=X_B_TRANSITION_FUNC,
    head=1,
)