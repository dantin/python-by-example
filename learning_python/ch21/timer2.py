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


def total(func, *args, **kwargs):
    """Total time to run func() reps times.
    Returns (total time, last result)
    """
    _reps = kwargs.pop('_reps', 1000)
    repslist = list(range(_reps))
    start = timer()
    for i in repslist:
        ret = func(*args, **kwargs)
    elapsed = timer() - start
    return (elapsed, ret)


def bestof(func, *args, **kwargs):
    """Quickest func() among reps runs.
    Returns (best time, last result)
    """
    _reps = kwargs.pop('_reps', 5)
    best = 2 ** 32
    for i in range(reps):
        start = timer()
        ret = func(*args, **kwargs)
        elapsed = timer() - start
        if elapsed < best: best = elapsed
    return (best, ret)


def bestoftotal(func, *args, **kwargs):
    """Best of totals:
    (best of reps1 runs of (total of reps2 runs of func))
    """
    _reps1 = kwargs.pop('_reps1', 5)
    return min(total(func, *args, **kwargs) for i in range(_reps1))
