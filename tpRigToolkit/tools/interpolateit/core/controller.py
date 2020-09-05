#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Interpolate It widget controller class implementation
"""

from __future__ import print_function, division, absolute_import


class InterpolateItController(object):
    def __init__(self, client, model):
        super(InterpolateItController, self).__init__()

        self._client = client
        self._model = model

    @property
    def client(self):
        return self._client

    @property
    def model(self):
        return self._model
