# -*- coding: utf-8 -*-

"""
    pyap.utils
    ~~~~~~~~~~~~~~~~

    This module provides some utility functions.

    :copyright: (c) 2015 by Vladimir Goncharov.
    :license: MIT, see LICENSE for more details.
"""

import re
from .packages import six


if six.PY2:

    def match(regex, string, flags=0):
        '''Utility function for re.match '''
        if isinstance(string, str):
            string = unicode(string, 'utf-8')
        return re.match(
            unicode(regex, 'utf-8'),
            string,
            flags=flags
        )

    def findall(regex, string, flags=0):
        '''Utility function for re.findall '''
        if isinstance(string, str):
            string = unicode(string, 'utf-8')
        return re.findall(
            unicode(regex, 'utf-8'),
            string,
            flags=flags
        )

    def unicode_str(string):
        '''Return Unicode string'''
        return unicode(string, 'utf-8')

elif six.PY3:

    def match(regex, string, flags=0):
        '''Utility function for re.match '''
        ret = re.match(regex[0], string, flags=flags)
        if not ret:
            ret = re.match(regex[1], string, flags=flags)
            if not ret:
                ret = re.match(regex[2], string, flags=flags)
            return ret
        else:
            return ret

    def findall(regex, string, flags=0):
        '''Utility function for re.findall '''
        ret = [(0,m) for m in re.findall(regex[0], string, flags=flags)]
        if len(ret) == 0:
            ret = [(1,m) for m in re.findall(regex[1], string, flags=flags)]
            ret += [(2,m) for m in re.findall(regex[2], string, flags=flags)]
            return ret
        else:
            return ret

    def unicode_str(string):
        '''Return Unicode string'''
        return string
