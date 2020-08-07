import random as rnd
import time
import numpy as np
from cli_tables.cli_tables import *
from Vector2D import Vector2D
from progress.bar import Bar

# workload-size
N = 100000  # max number size
loops = 300000  # amount of additions

# sampling
samplesize = 10


def getCurrentTime():
    return time.time_ns() / (10 ** 9)


def rndValue():
    return rnd.randint(0, N)


def vectorSpeedTest():
    t0 = getCurrentTime()
    a = Vector2D(0, 0)

    for x in range(loops):
        a = a + Vector2D(rndValue(), rndValue())

    return getCurrentTime() - t0


def tupleSpeedTest():
    t0 = getCurrentTime()
    a = (0, 0)

    for x in range(loops):
        b = (rndValue(), rndValue())
        a = (a[0] + b[0], a[1] + b[1])

    return getCurrentTime() - t0


def npSpeedTest():
    t0 = getCurrentTime()
    a = np.array([0, 0])

    for x in range(loops):
        a = a + np.array([rndValue(), rndValue()])

    return getCurrentTime() - t0


if __name__ == "__main__":
    vectortimes = list()
    tupletimes = list()
    nparraytimes = list()

    bar = Bar('Vector2D', max=samplesize)
    for i in range(samplesize):
        vectortimes.append(vectorSpeedTest())
        bar.next()
    bar.finish()

    bar = Bar('Tuple   ', max=samplesize)
    for i in range(samplesize):
        tupletimes.append(tupleSpeedTest())
        bar.next()
    bar.finish()

    bar = Bar('np.Array', max=samplesize)
    for i in range(samplesize):
        nparraytimes.append(npSpeedTest())
        bar.next()
    bar.finish()

    print_table([['time [s]', 'avg', 'var'],
                 ['Vector2D', "%.2G" % np.mean(vectortimes), "%.2G" % np.var(vectortimes)],
                 ['Tuple', "%.2G" % np.mean(tupletimes), "%.2G" % np.var(tupletimes)],
                 ['np.array', "%.2G" % np.mean(nparraytimes), "%.2G" % np.var(nparraytimes)]])
