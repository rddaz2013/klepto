"""
test speed and effectiveness of a selection of cache algorithms
"""

from klepto.archives import file_archive
from random import choice

def _test_hits(algorithm, maxsize=20, keymap=None,
               rangelimit=5, tries=1000, archived=False):

    @algorithm(maxsize=maxsize, keymap=keymap)
    def f(x, y):
        return 3*x+y

    if archived:
        f.archive(file_archive('cache.pkl'))

    domain = list(range(rangelimit))
    domain += [float(i) for i in domain]
    for i in range(tries):
        r = f(choice(domain), choice(domain))

    f.dump()
    return f.info()


if __name__ == '__main__':

    from klepto import *
   #from klepto.safe import *

    print ("WITHOUT ARCHIVE")
    for cache in [rr_cache,mru_cache,lru_cache,lfu_cache,inf_cache,no_cache]:
        msg = cache.__name__ + ":"
        msg += "%s" % str(_test_hits(cache, maxsize=1000, rangelimit=50))
        print (msg)

    print ("\nWITH ARCHIVE")
    for cache in [rr_cache,mru_cache,lru_cache,lfu_cache,inf_cache,no_cache]:
        msg = cache.__name__ + ":"
        msg += "%s" % str(_test_hits(cache, maxsize=1000, rangelimit=50, archived=True))
        print (msg)

# EOF
