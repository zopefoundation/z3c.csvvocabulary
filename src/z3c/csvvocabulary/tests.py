##############################################################################
#
# Copyright (c) 2006 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
import doctest
import re
import unittest
from pprint import pprint

from zope.testing import renormalizing


checker = renormalizing.RENormalizing([
    # Python 2 unicode strings add a "u".
    (re.compile("u('.*?')"),
     r"\1"),
    # Python 3 renamed type to class.
    (re.compile("<type "),
     r"<class "),
])


def test_suite():
    return unittest.TestSuite([
        doctest.DocFileSuite(
            'README.rst',
            optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS,
            globs={'pprint': pprint},
            checker=checker,
        ),
    ])
