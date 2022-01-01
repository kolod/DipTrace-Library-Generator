#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright 2021-... Oleksandr Kolodkin <alexandr.kolodkin@gmail.com>.
# This program is distributed under the MIT license.
# Glory to Ukraine!

import unittest
import DipTrace


class TestPoint(unittest.TestCase):

	def test_point_1(self):
		x = DipTrace.Point()
		self.assertEqual('<Item X="0" Y="0"/>\n', str(x))

	def test_point_2(self):
		y = DipTrace.Point(x=10.0, y=20.0)
		self.assertEqual('<Item X="10" Y="20"/>\n', str(y))

	def test_point_3(self):
		z = DipTrace.Point()
		z.x = 10.5
		z.y = 20.5
		self.assertEqual('<Item X="10.5" Y="20.5"/>\n', str(z))
