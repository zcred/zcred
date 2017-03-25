#!/usr/bin/env python

"""
test_zcred
----------

Tests for the `zcred` module.
"""

import unittest
import zcred

class TestZcred(unittest.TestCase):
    def test_decode(self):
        zcred.decode("world!")
        pass
