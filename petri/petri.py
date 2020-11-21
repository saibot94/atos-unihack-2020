from argparse import ArgumentParser
from typing import List
import random
from datetime import datetime
from models import Place, Token, Transition
from input_data import TRANSITIONS

parser = ArgumentParser()
parser.add_argument("--iterations", default=10, type=int)





def main():
    args = parser.parse_args()
    for i in range(args.iterations):
        deletions = []
        creations = []
        for t in TRANSITIONS:
            t.tick(i, deletions, creations)
        for node in deletions:
            node.pop_token()
        for output_node, new_token in creations:
            output_node.add_token(new_token)
    pass


if __name__ == "__main__":
    main()