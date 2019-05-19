#!/usr/bin/env python3

import sys


def generate_proposal(member, coin):
    if member == 0:
        yield [coin]
    else:
        for i in range(coin, -1, -1):
            for proposal in generate_proposal(member - 1, coin - i):
                yield [i] + proposal


def main(num_pirates, coin):

    optimal_proposal = []

    for member in range(num_pirates):
        best_coin = -1
        best_proposal = None
        optimal_proposal.append(-1)
        for proposal in generate_proposal(member, coin):
            vote = sum(1 for i in range(member + 1) if proposal[i] > optimal_proposal[i])
            if vote * 2 >= (member + 1) and proposal[-1] > best_coin:
                best_coin = proposal[-1]
                best_proposal = proposal

        if best_proposal:
            optimal_proposal = best_proposal

        print(member + 1, optimal_proposal)


if __name__ == '__main__':
    main(int(sys.argv[1]), int(sys.argv[2]))