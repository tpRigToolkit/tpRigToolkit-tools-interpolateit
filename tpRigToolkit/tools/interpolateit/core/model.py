#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Interpolate It widget model class implementation
"""

from __future__ import print_function, division, absolute_import

from Qt.QtCore import *


class InterpolateItModel(QObject, object):
    def __init__(self):
        super(InterpolateItModel, self).__init__()
