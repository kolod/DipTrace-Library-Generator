#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright 2021-... Oleksandr Kolodkin <alexandr.kolodkin@gmail.com>.
# This program is distributed under the MIT license.
# Glory to Ukraine!

import unittest
import DipTrace


class TestPoint(unittest.TestCase):

	def test_origin_1(self):
		x = DipTrace.Origin()
		self.assertEqual('<Origin X="0" Y="0"/>\n', str(x))

	def test_origin_2(self):
		y = DipTrace.Origin(x=10.0, y=20.0)
		self.assertEqual('<Origin X="10" Y="20"/>\n', str(y))

	def test_origin_3(self):
		z = DipTrace.Origin()
		z.x = 10.5
		z.y = 20.5
		self.assertEqual('<Origin X="10.5" Y="20.5"/>\n', str(z))

	def test_pattern_origin_1(self):
		expected = '<Origin X="0" Y="0" Cross="Y" Circle="Y" Common="Hide" Courtyard="Show"/>\n'
		actual = DipTrace.Origin(
			cross=True,
			circle=True,
			common=DipTrace.Visible.Hide,
			courtyard=DipTrace.Visible.Show
		)
		self.assertEqual(expected, str(actual))
		self.assertEqual(True, actual.cross)
		self.assertEqual(True, actual.circle)
		self.assertEqual(DipTrace.Visible.Hide, actual.common)
		self.assertEqual(DipTrace.Visible.Show, actual.courtyard)

	def test_pattern_origin_2(self):
		expected = '<Origin X="-21.2" Y="5" Cross="N" Circle="N" Common="Show" Courtyard="Hide"/>\n'
		actual = DipTrace.Origin(
			x=-21.2,
			y=5,
			cross=False,
			circle=False,
			common=DipTrace.Visible.Show,
			courtyard=DipTrace.Visible.Hide
		)
		self.assertEqual(expected, str(actual))
		self.assertEqual(False, actual.cross)
		self.assertEqual(False, actual.circle)
		self.assertEqual(DipTrace.Visible.Show, actual.common)
		self.assertEqual(DipTrace.Visible.Hide, actual.courtyard)

		actual.cross = None
		actual.circle = None
		actual.common = None
		actual.courtyard = None

		self.assertEqual(None, actual.cross)
		self.assertEqual(None, actual.circle)
		self.assertEqual(None, actual.common)
		self.assertEqual(None, actual.courtyard)


