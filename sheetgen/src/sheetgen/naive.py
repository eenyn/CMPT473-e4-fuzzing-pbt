"""Phase 2: a naive random-derivation generator.

TODO(students): implement generate(), following this rule exactly:

  * Start from START and repeatedly expand the leftmost remaining
    nonterminal until only text remains; join the text in order.
  * Depth: START has depth 0, and each symbol in an expansion has depth one
    more than the nonterminal it replaced.
  * A nonterminal shallower than max_depth: choose uniformly at random among
    all of its expansions in GRAMMAR.
  * A nonterminal at depth max_depth or deeper: choose uniformly at random
    among cheapest_expansions(symbol).

This always finishes. Grading checks that the sheets your generator writes
are distributed like those of this rule, so do not add weights, filters or
other knowledge of the language: improvements belong in adapted.py.

Hint: a stack of (symbol, depth) pairs, with each expansion pushed in
reverse order, expands the leftmost symbol first.
"""

from __future__ import annotations

import random

from sheetgen.grammar import (  # noqa: F401 (for your implementation)
    GRAMMAR,
    START,
    cheapest_expansions,
    is_nonterminal,
)


def generate(rng: random.Random, *, max_depth: int = 20) -> str:
    """Returns one sheet derived at random from GRAMMAR.

    All randomness must come from `rng`, so that a seed reproduces a corpus.
    """
    input = []                  # working list of terminal symbols
    symList = [(START, 0)]      # stack of tuples containing (nonterminal: Symbol, depth: int)
    debug = False

    # continue looping until all symbols processed
    while symList:
        (symbol, depth) = symList.pop()     # check leftmost symbol
        if debug: print("popping from symList: ("+symbol+","+str(depth)+")")

        # symbol is nonterminal, process
        if is_nonterminal(symbol):
            if debug: print("symbol nonterminal: "+symbol)
            if depth >= max_depth:
                if debug: print("max depth reached: "+str(depth)+" >= "+str(max_depth))
                # choose randomly from cheapest expansions
                # gramTuple = cheapest_expansions(symbol)[rng.randint(0, len(GRAMMAR[symbol])-1)]
                gramTuple = rng.choice(cheapest_expansions(symbol))
            else:
                if debug: print("depth ok: "+str(depth)+" < "+str(max_depth))
                # choose randomly from all expansions
                # gramTuple = GRAMMAR[symbol][rng.randint(0, len(GRAMMAR[symbol])-1)]
                gramTuple = rng.choice(GRAMMAR[symbol])

            # push backwards onto stack (leftmost symbol focus)
            if debug: print("gramTuple chosen: ("+','.join(gramTuple)+")")
            for newSym in reversed(gramTuple):
                if debug: print("appending new tuple to symList: ("+newSym+","+str(depth+1)+")")
                symList.append((newSym, depth+1))

        # symbol is terminal, add to generated input
        else:
            if debug: print("symbol terminal, adding to input: "+symbol)
            input.append(symbol)
            if debug: print("current input: "+''.join(input))

    # recombine strings into generated sheet string
    return ''.join(input)

    # while not hasNonTerm:
    #     hasNonTerm = False
    #     depth += 1
    #     symList = input.split()
    #     # iterate thru relevant terms in the string
    #     for symbol in symList:
    #         if is_nonterminal(symbol):
    #             hasNonTerm = True
    #             if depth > max_depth:
    #                 # choose randomly from cheapest expansions
    #                 symbol = cheapest_expansions(symbol)[rng.randint(0, len(GRAMMAR[symbol])-1)]
    #             else:
    #                 # choose randomly from all expansions
    #                 symbol = GRAMMAR[symbol][rng.randint(0, len(GRAMMAR[symbol])-1)]
    #             break   # focus leftmost symbols first
    #     # recombine symbols into full string (keep array flat)
    #     input = ' '.join(symList)
    # return input
        
