from typing import Set, Tuple, Dict, List
from collections import namedtuple
from tqdm import tqdm

# We use a slightly modified definition of a Turing machine from Wikipedia.
# A Turing machine M is a 7-tuple
# - Q: a finite set of states
# - A: a finite set of tape alphabet symbols
# - b \elem A: the blank symbol
# - T: initial tape
# - q \elem Q: the initial state
# - F \subseteq Q: the set of final states, the set of states that will cause the machine to halt
# - t: (Q \ F) * A -> Q * A * {L,R}
#       the transition function where L is left shift of the head and R is right shift of the head
#       from the Wikipedia article: "If the transition function is not defined on the current state and the current tape symbol, then the machine halts;
#       intuitively, the transition function specifies the next state transited from the current state, which symbol to overwrite the current symbol pointed by the head, and the next head movement."

# Note that we will represent states and symbols by strings


class TuringMachine:
    def __init__(
        self,
        states: Set[str],
        alphabet: Set[str],
        blank_symbol: str,
        initial_tape: List[str],
        initial_state: str,
        final_states: Set[str],
        transition_func: Dict,
        head: int = 0,
    ):
        self.states = states
        self.alphabet = alphabet
        if blank_symbol not in alphabet:
            raise ValueError("error! given blank symbol is not in given alphabet")
        self.blank_symbol = blank_symbol
        if initial_tape:
            for sym in initial_tape:
                if sym not in alphabet:
                    raise ValueError("error! unknown symbol in given initial tape!")
        self.initial_tape = initial_tape
        if initial_state not in states:
            raise ValueError("error! given initial state not in given set of states")
        self.initial_state = initial_state
        if not final_states.issubset(states):
            raise ValueError(
                "error! given final states not a subset of given set of states"
            )
        self.final_states = final_states
        self.transition_func = transition_func
        self.tape = Tape(blank_symbol=self.blank_symbol, initial_tape=self.initial_tape)
        self.head_ = head
        self.current_state_ = initial_state

    def run(self, max_iter, verbose=True):
        def update_():
            self.current_state, self.current_state, head_dir = self.transition_func[
                (self.current_state, self.tape[self.head_])
            ]
            self.head_ += 1 if head_dir == "L" else -1

        if verbose:
            curr_tape = []
        else:
            for i in tqdm(range(max_iter)):
                update()

class Tape:
    def __init__(self, blank_symbol, initial_tape=None):
        self.tape = dict()
        self.blank_symbol = blank_symbol
        if initial_tape:
            for n, sym in enumerate(initial_tape):
                self.tape[n] = sym

    def __getitem__(self, key):
        return self.tape[key] if key in self.tape else self.blank_symbol

    def __setitem__(self, key, item):
        self.tape[key] = item


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
    transition_func={
        ("s1", "B"): ("s2", "X", "R"),
        ("s2", "B"): ("s3", "B", "L"),
        ("s3", "X"): ("s4", "B", "R"),
        ("s4", "B"): ("s1", "B", "L"),
    },
    head=0,
)
