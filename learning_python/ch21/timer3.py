# -*- coding: utf-8 -*-
"""total(spam, 1, 2, a=3, b=4, _reps=1000) calls and times spam(1, 2, a=3, b=4)
_reps times, and returns total time for all runs, with final result.

bestof(spam, 1, 2, a=3, b=4, _reps=5) runs best-of-N timer to attempt to
filter out system load variation, and returns best time amount _reps tests.


bestoftotal(spam, 1, 2, a=3, b=4, _reps1=5, _reps2=1000) runs best-of-totals
test, which takes the best amount _reps1 runs of (the total of _reps runs);
"""

import sys
import time


timer = time.clock if sys.platform[:3] == 'win' else time.time


def total(func, *args, _reps=1000, **kwargs):
    """Total time to run func() reps times.
    Returns (total time, last result)
    """
    start = timer()
    for i in range(_reps):
        ret = func(*args, **kwargs)
    elapsed = timer() - start
    return (elapsed, ret)


def bestof(func, *args, _reps=5, **kwargs):
    """Quickest func() among reps runs.
    Returns (best time, last result)
    """
    best = 2 ** 32
    for i in range(reps):
        start = timer()
        ret = func(*args, **kwargs)
        elapsed = timer() - start
        if elapsed < best: best = elapsed
    return (best, ret)


def bestoftotal(func, *args, _reps1=5, **kwargs):
    """Best of totals:
    (best of reps1 runs of (total of reps2 runs of func))
    """
    return min(total(func, *args, **kwargs) for i in range(_reps1))
