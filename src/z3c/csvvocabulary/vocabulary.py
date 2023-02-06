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
"""CSV Vocabulary Implementation"""
import csv
import os.path

from zope.i18nmessageid import MessageFactory
from zope.schema import vocabulary


_ = MessageFactory('zope')


def CSVVocabulary(filename, messageFactory=_, encoding='latin1'):
    # Create a prefix
    prefix = os.path.split(filename)[-1][:-4]
    # Open a file and read the data
    f = open(filename, encoding=encoding)
    reader = csv.reader(f, delimiter=";")
    # Create the terms and the vocabulary
    terms = []
    for id, title in reader:
        term = vocabulary.SimpleTerm(
            id, title=messageFactory(prefix+'-'+id, default=title))
        terms.append(term)
    f.close()
    return vocabulary.SimpleVocabulary(terms)
