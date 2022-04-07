#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright 2021-... Oleksandr Kolodkin <alexandr.kolodkin@gmail.com>.
# This program is distributed under the MIT license.
# Glory to Ukraine!

import unittest
import DipTrace


class TestDimension(unittest.TestCase):

	def test_constructor_1(self):
		expected = \
			'<Dimension Enabled="Y" Locked="Y" Type="Horizontal" ' \
			'Connected1="-1" Object1="0" SubObject1="0" Point1="0" ' \
			'Connected2="-1" Object2="0" SubObject2="0" Point2="0" Layer="Top Dimension" ' \
			'X1="0" Y1="0" X2="0" Y2="0" XD="0" YD="0" ArrowSize="0.667" Units="Common" ' \
			'FontVector="Y" FontName="Tahoma" FontSize="2" FontScale="1" FontWidth="-2" ShowUnits="N" Angle="0" ' \
			'ExternalRadius="0" PointerMode="0"/>\n'
		actual = DipTrace.Dimension()
		self.assertEqual(expected, str(actual))

	def test_constructor_2(self):
		expected = \
			'<Dimension Enabled="Y" Locked="Y" Type="Pointer" ' \
			'Connected1="1" Object1="2" SubObject1="3" Point1="4" ' \
			'Connected2="-1" Object2="0" SubObject2="0" Point2="0" Layer="Bottom Dimension" ' \
			'X1="-1.27" Y1="0" X2="1.27" Y2="0" XD="0" YD="5" ArrowSize="0.8" Units="mm" ' \
			'FontVector="N" FontName="Courier New" FontSize="9" FontScale="1" FontWidth="-2" ShowUnits="N" Angle="0" ' \
			'ExternalRadius="1" PointerMode="1">\n' \
			'  <PointerText>Sample</PointerText>\n' \
			'</Dimension>\n'
		actual = DipTrace.Dimension(
			enabled=True,
			locked=True,
			type=DipTrace.DimensionType.Pointer,
			connection_1=DipTrace.Connection(1, 2, 3, 4),
			connection_2=DipTrace.Connection(-1, 2, 3, 4),
			layer=DipTrace.LayerType.BottomDimension,
			point_1=DipTrace.Point(x=-1.27, y=0),
			point_2=DipTrace.Point(x=1.27, y=0),
			point_d=DipTrace.Point(x=0.0, y=5),
			arrow_size=0.8,
			units=DipTrace.DimensionUnits.mm,
			font=(False, 'Courier New', 9, 1.0, -2, False),
			angle=0.0,
			pointer_mode=1,
			text='Sample',
			radius=1.0
		)
		self.assertEqual(expected, str(actual))
		self.assertEqual(True, actual.enabled)
		self.assertEqual(True, actual.locked)
		self.assertEqual(DipTrace.DimensionType.Pointer, actual.type)
		self.assertEqual(DipTrace.Connection(1, 2, 3, 4), actual.connection_1)
		self.assertEqual(DipTrace.Connection(-1, 0, 0, 0), actual.connection_2)
		self.assertEqual(DipTrace.LayerType.BottomDimension, actual.layer)
		self.assertEqual(-1.27, actual.point_1.x)
		self.assertEqual(1.27, actual.point_2.x)
		self.assertEqual(5.0, actual.point_d.y)
		self.assertEqual(0.8, actual.arrow_size)
		self.assertEqual(DipTrace.DimensionUnits.mm, actual.units)
		self.assertEqual((False, 'Courier New', 9, 1.0, -2, False), actual.font)
		self.assertEqual(0.0, actual.angle)
		self.assertEqual(1, actual.pointer_mode)
		self.assertEqual('Sample', actual.text)
		self.assertEqual(1.0, actual.radius)
		self.assertEqual('(Connected=1, Object=2, SubObject=3, Point=4)', str(actual.connection_1))

		actual.text = None
		self.assertEqual(None, actual.text)

		actual.text = 'text'
		actual.pointer_mode = 0
		actual.normalize()
		self.assertEqual(None, actual.text)
