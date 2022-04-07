#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright 2021-... Oleksandr Kolodkin <alexandr.kolodkin@gmail.com>.
# This program is distributed under the MIT license.
# Glory to Ukraine!

import unittest
import DipTrace


class TestTerminal(unittest.TestCase):

	def test_constructor_1(self):
		expected = \
			'<Terminal Shape="Rectangle" X="0" Y="0" Angle="0" Width="0" Height="0"/>\n'
		actual = DipTrace.Terminal()
		self.assertEqual(expected, str(actual))

	def test_constructor_2(self):
		expected = \
			'<Terminal Shape="Polygon" X="0" Y="0" Angle="0" Width="0.1" Height="0.1">\n' \
			'  <Points>\n' \
			'    <Item X="0.231" Y="0.0957"/>\n' \
			'    <Item X="0.231" Y="-0.0957"/>\n' \
			'    <Item X="0.0957" Y="-0.231"/>\n' \
			'  </Points>\n' \
			'</Terminal>\n'

		actual = DipTrace.Terminal(
			shape=DipTrace.TerminalShape.Polygon,
			width=0.1,
			height=0.1,
			points=[
				DipTrace.Point(x=0.231, y=0.0957),
				DipTrace.Point(x=0.231, y=-0.0957),
				DipTrace.Point(x=0.0957, y=-0.231)
			]
		)
		self.assertEqual(expected, str(actual))
		self.assertEqual(DipTrace.TerminalShape.Polygon, actual.shape)

		x = actual.points
		print(x)

		self.assertEqual(0.231, actual.points[0].x)
