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

        # for node, token in deletions:
        #     node.remove_token(token)
    pass


if __name__ == "__main__":
    main()