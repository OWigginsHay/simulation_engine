import pstats
from pstats import SortKey

p = pstats.Stats('prof.pyprof')
p.strip_dirs().sort_stats(-1).print_stats()

p.sort_stats(SortKey.NAME)
p.print_stats()

