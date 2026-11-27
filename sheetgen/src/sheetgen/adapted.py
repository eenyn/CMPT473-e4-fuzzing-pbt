"""Phase 2 adaptation: your improved generator.

TODO(students): implement generate().

Before changing anything, write down your hypothesis: which pipeline stage
or code your change should reach, and why the naive generator cannot. Then
make one targeted change and measure its effect with run-trials and covtrace.

You may reuse code from naive.py.
"""

from __future__ import annotations

import random


def generate(rng: random.Random, *, max_depth: int = 20) -> str:
    """Returns one sheet. All randomness must come from `rng`."""
    raise NotImplementedError("Phase 2: implement your adapted generator")
