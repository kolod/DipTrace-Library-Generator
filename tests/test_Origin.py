#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright 2021-... Oleksandr Kolodkin <alexandr.kolodkin@gmail.com>.
# This program is distributed under the MIT license.
# Glory to Ukraine!

import unittest
import DipTrace


class TestPoint(unittest.TestCase):

	def __init__(self, *args, **kwargs):
		self.x = DipTrace.Origin()
		self.y = DipTrace.Origin(10.0, 20.0)
		self.z = DipTrace.Origin()
		self.z.x = 10.5
		self.z.y = 20.5
		super().__init__(*args, **kwargs)

	def test_point(self):
		self.assertEqual('<Origin X="0" Y="0"/>\n', str(self.x))
		self.assertEqual('<Origin X="10" Y="20"/>\n', str(self.y))
		self.assertEqual('<Origin X="10.5" Y="20.5"/>\n', str(self.z))
