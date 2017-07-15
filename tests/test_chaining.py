#!/usr/bin/env python
#
# Author: Mike McKerns (mmckerns @caltech and @uqfoundation)
# Copyright (c) 2013-2016 California Institute of Technology.
# Copyright (c) 2016-2017 The Uncertainty Quantification Foundation.
# License: 3-clause BSD.  The full license text is available at:
#  - http://trac.mystic.cacr.caltech.edu/project/pathos/browser/klepto/LICENSE

import sys
from klepto.keymaps import *
from klepto.crypto import *
h = hashmap(algorithm='md5')
p = picklemap(serializer='dill')
hp = p + h

def test_chaining():
    assert p(1) == pickle(1, serializer='dill')
    assert h(1) == 'c4ca4238a0b923820dcc509a6f75849b'
    if sys.version_info[0] == 2:
        assert hp(1) == 'ee7f32117eab97ec5460313282938c93'
    else: #XXX: different, because 3.x returns b'' while 2.x returns ''
        assert hp(1) == 'a2ed37e4f2f0ccf8be170d8c31c711b2'
    assert h(p(1)) == hp(1)
    assert hp.inner(1) == p(1)
    assert hp.outer(1) == h(1)
    assert bool(h.inner) == False
    assert bool(p.inner) == False
    assert bool(hp.inner) == True
    assert bool(h.outer) == False
    assert bool(p.outer) == False
    assert bool(hp.outer) == True


if __name__ == '__main__':
    test_chaining()
