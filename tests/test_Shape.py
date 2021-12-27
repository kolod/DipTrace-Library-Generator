#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright 2021-... Oleksandr Kolodkin <alexandr.kolodkin@gmail.com>.
# This program is distributed under the MIT license.
# Glory to Ukraine!

import unittest
import DipTrace


class TestShape(unittest.TestCase):

	def test_constructor(self):
		expected = '<Shape Type="Line" LineWidth="0.25" Enabled="Y" Locked="Y"/>\n'
		actual = DipTrace.Shape()
		self.assertEqual(expected, str(actual))

	def test_line(self):
		expected = \
			'<Shape Type="Line" LineWidth="0.25" Enabled="Y" Locked="Y">\n' \
			'  <Points>\n' \
			'    <Item X="-2.54" Y="0"/>\n' \
			'    <Item X="2.54" Y="0"/>\n' \
			'  </Points>\n' \
			'</Shape>\n'

		actual = DipTrace.Shape()
		actual.add_points([
			DipTrace.Point(-2.54, 0),
			DipTrace.Point(2.54, 0)
		])

		self.assertEqual(expected, str(actual))

	def test_polyline(self):
		expected = \
			'<Shape Type="Polyline" LineWidth="0.25" Enabled="Y" Locked="Y">\n' \
			'  <Points>\n' \
			'    <Item X="-1.0999" Y="1.27"/>\n' \
			'    <Item X="1.0999" Y="0"/>\n' \
			'    <Item X="-1.0999" Y="-1.27"/>\n' \
			'    <Item X="-1.0999" Y="1.27"/>\n' \
			'  </Points>\n' \
			'</Shape>\n'

		actual = DipTrace.Shape(shape_type=DipTrace.Shape.ShapeType.Polyline)
		actual.add_points([
			DipTrace.Point(-1.0999, 1.27),
			DipTrace.Point(1.0999, 0),
			DipTrace.Point(-1.0999, -1.27),
			DipTrace.Point(-1.0999, 1.27)
		])

		self.assertEqual(expected, str(actual))


if __name__ == '__main__':
	unittest.main()

