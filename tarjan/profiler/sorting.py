import random
import sets
import time
from profiler import Profiler

class SortingProfiler(Profiler):

    MIN_NUM = 0
    MAX_NUM = 3142545425234543

    def __init__(self, algorithm, list = None, size = 10, unique = True,
                 comp = True, swap = True, trace = False):
        """
        creates an instance of the test of the algorithm for a profiler
        :param algorithm: the algorithm being profiled
        :param list: allows the client to use her own list
        :param size: the size of a list, 10 by default
        :param unique: if True, list contains unique integers
        :param comp: if True, count comparisons
        :param swap: if True, count swaps
        :param trace: if True, print the trace of the algorithm (list after each exchange)
        :return: a new profiler object

        Run the function with the given parameters and print its profile
        results.
        """
        self._list = list
        self._size = size
        self._unique = unique
        self._comp = comp
        self._swap = swap
        self._trace = trace
        self._swap_count = 0
        self._comp_count = 0
        self._algorithm = algorithm
        self._start = 0
        self._elapsed_time = 0

    def test(self):
        if self._list == None:
            self._make_random_list()

        self._start_clock()
        self._run()
        self._stop_clock()
        print self

    def _make_random_list(self):
        if self._unique:
            s = sets.Set()
            while len(s) != self._size:
                s.add(random.randint(self.MIN_NUM, self.MAX_NUM))
            self._list = list(s)
        else:
            n = 0
            while n != self._size:
                self._list.append(random.randint(self.MIN_NUM, self.MAX_NUM))
                n += 1

        random.shuffle(self._list)

    def swap(self):
        """ Counts exchanges if on. """
        if self._swap:
            self._swap_count += 1
        if self._trace:
            print self._list

    def comparison(self):
        """ Counts comparisons if on. """
        if self._comp:
            self._comp_count += 1

    def _start_clock(self):
        """ Record the starting time. """
        self._start = time.time()

    def _stop_clock(self):
        """
        Stops the clock and computes the elapsed time in seconds,
        to the nearest millisecond.
        """
        self._elapsed_time = time.time() - self._start

    def _run(self):
        """ Runs the sorting algorithm. """
        self._algorithm(self._list, self)

    def __str__(self):
        """ Returns the results as a string. """
        result = "Problem size: "
        result += str(len(self._list)) + "\n"
        result += "Elapsed time: "
        result += str(self._elapsed_time) + "\n"
        if self._comp:
            result += "Comparisons:  "
            result += str(self._comp_count) + "\n"
        if self._swap:
            result += "Exchanges:    "
            result += str(self._swap_count) + "\n"
        return result
