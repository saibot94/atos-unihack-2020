from argparse import ArgumentParser
from typing import List
import random
from datetime import datetime


parser = ArgumentParser()
parser.add_argument("--iterations", default=10, type=int)

VERBOSE = 1


class LoggableEntry:
    _log = []

    # def __init__(self):
    #     _log = []

    def log(self, message):
        formatted = f"[{datetime.utcnow()}] {self.__str__()}: {message}"
        self._log.append(formatted)
        if VERBOSE:
            print(formatted)


class Token(LoggableEntry):
    def __init__(self, id):
        super(LoggableEntry, self).__init__()
        self.id = id

    def __str__(self):
        return f"Token {self.id}"


class Place(LoggableEntry):
    def __init__(self, id, capacity: int, tokens: List[Token]):
        super(LoggableEntry, self).__init__()
        self.capacity = capacity
        self.id = id
        self.tokens = tokens
        self.deleted_tokens = []

    def has_token(self):
        if len(self.tokens) > 0:
            return True
        return False

    def has_space(self):
        """If there are less tokens than capacity"""
        return len(self.tokens) < self.capacity

    def __str__(self):
        return f"Place {self.id}"

    def add_token(self, token):
        self.tokens.append(token)
        self.log(f"Added token {token}. I have {len(self.tokens)}")

    def pop_token(self):
        token = self.tokens.pop()
        token.log("Going through transition, getting removed")
        self.log(f"Removed token {token}. I still have {len(self.tokens)} left")


class Transition(LoggableEntry):
    def __init__(self, id, inputs: List[Place], outputs: List[Place]):
        super(LoggableEntry, self).__init__()
        self.inputs = inputs
        self.id = id
        self.outputs = outputs
        self.selected_output = self.outputs[0]

    def __str__(self):
        return f"Transition {self.id}"

    def tick(self, i):
        if all(inp.has_token() for inp in self.inputs) and all(
            o.has_space() for o in self.outputs
        ):
            for inp in self.inputs:
                inp.pop_token()
            for outp in self.outputs:
                new_token = Token(random.randint(0, 100000))
                new_token.log(f"Created and added to {outp}")
                self.log(f"Added {new_token} to {outp}")
                outp.add_token(new_token)
            self.log(f"Ran transition {str(self)}")


t1_inputs = [Place(1, 10, [Token(1)]), Place(2, 10, [Token(2)])]

p3 = Place(3, 10, [])
p4 = Place(4, 10, [Token(1234)])

t1_outputs = [p3]

t2_inputs, t2_outputs = [p3], [p4]


TRANSITIONS = [
    Transition("t1", t1_inputs, t1_outputs),
    Transition("t2", t2_inputs, t2_outputs),
]


def main():
    args = parser.parse_args()
    for i in range(args.iterations):
        for t in TRANSITIONS:
            t.tick(i)
    pass


if __name__ == "__main__":
    main()