import time


class Profiler(object):

    def __init__(self, algorithm):
        '''
        creates an instance of the test of the algorithm for a profiler
        :param algorithm: the algorithm being profiled
        :param trace: if True, print the trace of the algorithm
        :return: a new profiler object

        Run the function with the given parameters and print its profile
        results.
        '''

        self._algorithm = algorithm
        self._start = 0
        self._elapsed_time = 0

    def test(self):
        self._start_clock()
        self._run()
        self._stop_clock()
        print self

    def _start_clock(self):
        self._start = time.time()

    def _stop_clock(self):
        self._elapsed_time = round(time.time() - self._start, 3)

    def _run(self):
        pass

    def __str__(self):
        pass



