#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright 2021-... Oleksandr Kolodkin <alexandr.kolodkin@gmail.com>.
# This program is distributed under the MIT license.
# Glory to Ukraine!

import unittest
import DipTrace


class TestShape(unittest.TestCase):

	def test_constructor(self):
		expected = \
			'<Shape Type="Line" Locked="Y"/>\n'
		actual = DipTrace.Shape()
		self.assertEqual(expected, str(actual))

	def test_line(self):
		expected = \
			'<Shape Type="Line" Locked="Y">\n' \
			'  <Points>\n' \
			'    <Item X="-2.54" Y="0"/>\n' \
			'    <Item X="2.54" Y="0"/>\n' \
			'  </Points>\n' \
			'</Shape>\n'

		actual = DipTrace.Shape(
			points=[
				DipTrace.Point(x=-2.54, y=0),
				DipTrace.Point(x=2.54, y=0)
			]
		)

		self.assertEqual(expected, str(actual))
		self.assertEqual(DipTrace.ShapeType.Line, actual.type)
		self.assertEqual(None, actual.width)
		self.assertEqual(None, actual.enabled)
		self.assertEqual(True, actual.locked)
		self.assertEqual(None, actual.group)

		actual.points = None
		self.assertEqual(None, actual.points)

	def test_polyline(self):
		expected = \
			'<Shape Type="Polyline" Locked="Y">\n' \
			'  <Points>\n' \
			'    <Item X="-1.0999" Y="1.27"/>\n' \
			'    <Item X="1.0999" Y="0"/>\n' \
			'    <Item X="-1.0999" Y="-1.27"/>\n' \
			'    <Item X="-1.0999" Y="1.27"/>\n' \
			'  </Points>\n' \
			'</Shape>\n'

		actual = DipTrace.Shape(
			type=DipTrace.ShapeType.Polyline,
			points=[
				DipTrace.Point(x=-1.0999, y=1.27),
				DipTrace.Point(x=1.0999, y=0),
				DipTrace.Point(x=-1.0999, y=-1.27),
				DipTrace.Point(x=-1.0999, y=1.27)
			]
		)

		self.assertEqual(expected, str(actual))

	def test_pattern_shape(self):
		expected = \
			'<Shape Type="Rectangle" Locked="Y" Layer="Top Silk" AllLayers="N">\n' \
			'  <Points>\n' \
			'    <Item X="-2.54" Y="2.54"/>\n' \
			'    <Item X="2.54" Y="-2.54"/>\n' \
			'  </Points>\n' \
			'</Shape>\n'

		actual = DipTrace.Shape(
			enabled=None,
			locked=True,
			group=None,
			width=None,
			type=DipTrace.ShapeType.Rectangle,
			layer=DipTrace.LayerType.TopSilk,
			all_layers=False,
			points=[
				DipTrace.Point(x=-2.54, y=2.54),
				DipTrace.Point(x=2.54, y=-2.54),
			]
		)

		self.assertEqual(expected, str(actual))
