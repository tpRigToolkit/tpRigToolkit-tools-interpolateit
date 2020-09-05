#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Interpolate It widget view class implementation
"""

from __future__ import print_function, division, absolute_import

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"


from tpDcc.libs.qt.core import base


class InterpolateItView(base.BaseWidget, object):
    def __init__(self, model, controller, parent=None):

        self._model = model
        self._controller = controller

        super(InterpolateItView, self).__init__(parent=parent)

        self.refresh()

    def ui(self):
        super(InterpolateItView, self).ui()
