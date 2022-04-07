#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright 2021-... Oleksandr Kolodkin <alexandr.kolodkin@gmail.com>.
# This program is distributed under the MIT license.
# Glory to Ukraine!

import unittest
import DipTrace


class TestPad(unittest.TestCase):

	def test_constructor_1(self):
		expected = \
			'<Pad PadType="" Enabled="Y" X="0" Y="0" Angle="0" Locked="N" Side="Top">\n' \
			'  <Number>1</Number>\n' \
			'</Pad>\n'
		actual = DipTrace.Pad()
		self.assertEqual(expected, str(actual))

	def test_constructor_2(self):
		expected = \
			'<Pad PadType="PadT0" Enabled="Y" X="0" Y="0" Angle="0" Locked="N" Side="Bottom">\n' \
			'  <Number>12</Number>\n' \
			'</Pad>\n'
		actual = DipTrace.Pad(
			type='PadT0',
			side=DipTrace.Side.Bottom,
			number='12'
		)
		self.assertEqual(expected, str(actual))
		self.assertEqual('PadT0', actual.type)
		self.assertEqual(DipTrace.Side.Bottom, actual.side)
		self.assertEqual('12', actual.number)




