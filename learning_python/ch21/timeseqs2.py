#-*- coding: utf-8 -*-
"""Test the relative speed of iteration tool alternatives"""

import sys
import timer


reps = 10000
repslist = list(range(reps))


def forLoop():
    res = []
    for x in repslist:
        res.append(x + 10)
    return res


def listComp():
    return [x + 10 for x in repslist]


def mapCall():
    return list(map((lambda x: x + 10), repslist))


def genExp():
    return list(x + 10 for x in repslist)


def genFunc():
    def gen():
        for x in repslist:
            yield x + 10
    return list(gen())



if __name__ == '__main__':
    print(sys.version)
    for test in (forLoop, listComp, mapCall, genExp, genFunc):
        (bestof, (total, result)) = timer.bestoftotal(5, 1000, test)
        print('%-9s: %.5f ==> [%s..%s]' % 
                (test.__name__, bestof, result[0], result[-1]))
