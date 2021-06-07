# Code from Destroy all Software screencast

X_B = {
    ("B", "s1"): ("X", "R", "s2"),
    ("B", "s2"): ("B", "L", "s3"),
    ("X", "s3"): ("B", "R", "s4"),
    ("B", "s4"): ("B", "L", "s1")
}

def simulate(instructions):
    tape = ["B", "B"]
    head = 0
    state = "s1"

    for _ in range(8):
        print(state.rjust(4) + ": " + "".join(tape))
        print("      " + " " * head + "^")

        tape[head], head_dir, state = instructions[(tape[head], state)]
        head += 1 if head_dir == "R" else -1

simulate(X_B)