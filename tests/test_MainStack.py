#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright 2021-... Oleksandr Kolodkin <alexandr.kolodkin@gmail.com>.
# This program is distributed under the MIT license.
# Glory to Ukraine!

import unittest
import DipTrace


class TestMainStack(unittest.TestCase):

	def test_constructor_1(self):
		expected = \
			'<MainStack Shape="Obround" Width="0" Height="0" XOff="0" YOff="0"/>\n'
		actual = DipTrace.MainStack()
		self.assertEqual(expected, str(actual))

	def test_constructor_2(self):
		expected = \
			'<MainStack Shape="Rectangle" Width="1.5" Height="1.5" XOff="1" YOff="1.2" Corner="1"/>\n'
		actual = DipTrace.MainStack(
			shape=DipTrace.PadShape.Rectangle,
			width=1.5,
			height=1.5,
			x_offset=1.0,
			y_offset=1.2,
			corner=1
		)
		self.assertEqual(expected, str(actual))
		self.assertEqual(DipTrace.PadShape.Rectangle, actual.shape)
		self.assertEqual(1.5, actual.width)
		self.assertEqual(1.5, actual.height)
		self.assertEqual(1.0, actual.x_offset)
		self.assertEqual(1.2, actual.y_offset)
		self.assertEqual(1, actual.corner)
