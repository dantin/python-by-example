# -*- coding: utf-8 -*-
"""
pybench_cases.py: Run pybench on a set of pythons and statements.

Select modes by editing this script or using command-line arguments (in
sys.argv): e.g., run a "$ python pybench_cases.py" to test just
one specific version on stmts, "pybench_cases.py -a" to test all pythons
listed, or a "py -3 pybench_cases.py -a -t" to trace command lines too.
"""

import sys
import pybench


pythons = [
    (1, '/usr/bin/python'),
    (1, '/usr/local/bin/python3.7'),
]

stmts = [
    (0, 0, "[ord(x) for x in 'spam' * 2500]"),
    (0, 0, "res = []\nfor x in 'spam' * 2500: res.append(ord(x))"),
    (0, 0, "$listif3(map(ord, 'spam' * 2500))"),
    (0, 0, "list(ord(x) for x in 'spam' * 2500)"),
    (0, 0, "{x ** 2 for x in range(1000)}"),
    (0, 0, "s = set()\nfor x in range(1000): s.add(x ** 2)"),
    (0, 0, "{x: x ** 2 for x in range(1000)}"),
    (0, 0, "d = {}\nfor x in range(1000): d[x] = x ** 2"),
    (1, 1, "len(str(2 ** 1000000))")
]

tracecmd = '-t' in sys.argv
pythons = pythons if '-a' in sys.argv else None
pybench.runner(stmts, pythons, tracecmd)
