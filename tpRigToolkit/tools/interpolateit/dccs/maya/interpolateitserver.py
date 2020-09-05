#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains tpRigToolkit-tools-interpolateit server implementation for Maya
"""

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"

import tpDcc as tp
from tpDcc.core import server

LOGGER = tp.LogsMgr().get_logger('tpRigToolkit-tools-interpolateit')


class InterpolateItServer(server.DccServer, object):

    PORT = 18231

    def _process_command(self, command_name, data_dict, reply_dict):
        super(InterpolateItServer, self)._process_command(command_name, data_dict, reply_dict)
