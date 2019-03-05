# -*- coding: utf-8 -*-
"""
pybench_cases.py: Run pybench on a set of pythons and statements.

Select modes by editing this script or using command-line arguments (in
sys.argv): e.g., run a "$ python pybench_cases.py" to test just
one specific version on stmts, "pybench_cases.py -a" to test all pythons
listed, or a "py -3 pybench_cases.py -a -t" to trace command lines too.
"""

import sys
import pybench2


pythons = [
    (1, '/usr/bin/python'),
    (1, '/usr/local/bin/python3.7'),
]

stmts = [
    (0, 0, '', '[x ** 2 for x in range(1000)]'),
    (0, 0, '', 'res = []\nfor x in range(1000): res.append(x ** 2)'),
    (0, 0, 'def f(x):\n\treturn x', "[f(x) for x in 'spam' * 2500]"),
    (0, 0, "def f(x):\n\treturn x", "res = []\nfor x in 'spam' * 2500:\n\tres.append(f(x))"),
    (0, 0, "L = [1, 2, 3, 4, 5]", "for i in range(len(L)): L[i] += 1"),
    (0, 0, "L = [1, 2, 3, 4, 5]", "i = 0\nwhile i < len(L):\n\tL[i] += 1\n\ti += 1"),
]

tracecmd = '-t' in sys.argv
pythons = pythons if '-a' in sys.argv else None
pybench2.runner(stmts, pythons, tracecmd)
