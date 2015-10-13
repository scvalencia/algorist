from algorithms.sorting import selection_sort
from profiler.sorting import SortingProfiler

p = SortingProfiler(selection_sort)
p.test()

p = SortingProfiler(selection_sort, size = 10)
p.test()
