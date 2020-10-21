# -*- coding: utf-8 -*-
# *****************************************************************************
#       Copyright (C) 2003-2006 Gary Bishop.
#       Copyright (C) 2006  Jorgen Stenarson. <jorgen.stenarson@bostream.nu>
#
#  Distributed under the terms of the BSD License.  The full license is in
#  the file COPYING, distributed as part of this software.
# *****************************************************************************
from __future__ import absolute_import, print_function, unicode_literals

from platform import system

from . import (
    clipboard,
    console,
    lineeditor,
    logger,
    modes,
    rlmain,
    unicode_helper,
)
from .rlmain import *

_S = system()

if _S.lower() != 'windows':
    raise RuntimeError('pyreadline3 is for Windows only, not {}.'.format(_S))

del system, _S
