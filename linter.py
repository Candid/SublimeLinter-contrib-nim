#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Roman Bataev
# Copyright (c) 2015 Roman Bataev
#
# License: MIT
#

"""This module exports the Nim plugin class."""

import os
import re
from SublimeLinter.lint import Linter, util


class Nim(Linter):

    """Provides an interface to nim."""

    syntax = 'nim'
    cmd = 'nim check'
    executable = None
    version_args = '--version'
    version_re = r'(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 0.11.2'

    # Example:
    # obj.nim(106, 3) Error: not all cases are covered

    @property
    def regex(self):
        filename = os.path.basename(self.view.file_name())
        r = (
            r'\((?P<line>\d+), (?P<col>\d+)\) '
            r'(?:(?P<error>Error: )|(?P<warning>(Warning:)|(Hint:) ))'
            r'(?P<message>.+)'
        )
        return re.compile(filename + r)

    multiline = False
    line_col_base = (1, 1)
    tempfile_suffix = '-'
    error_stream = util.STREAM_BOTH
    selectors = {}
    word_re = None
    defaults = {}
    inline_settings = None
    inline_overrides = None
    comment_re = None
