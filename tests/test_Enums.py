#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright 2021-... Oleksandr Kolodkin <alexandr.kolodkin@gmail.com>.
# This program is distributed under the MIT license.
# Glory to Ukraine!

import unittest
import DipTrace


class TestDipTraceEnum(unittest.TestCase):

	def test_from_str_1(self):
		expected = DipTrace.Side.Top
		actual = DipTrace.Side.from_str('Top')
		self.assertEqual(expected, actual)

	def test_from_str_2(self):
		expected = DipTrace.Side.Bottom
		actual = DipTrace.Side.from_str('Bottom')
		self.assertEqual(expected, actual)

	def test_from_str_3(self):
		self.assertRaisesRegex(ValueError, '"Side" enum not found for "XYZ"', DipTrace.Side.from_str, 'XYZ')
