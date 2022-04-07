#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright 2021-... Oleksandr Kolodkin <alexandr.kolodkin@gmail.com>.
# This program is distributed under the MIT license.
# Glory to Ukraine!

import unittest
import DipTrace


class TestPattern(unittest.TestCase):

	def test_constructor_1(self):
		expected = \
			'<Pattern RefDes="" Mounting="None" Width="0" Height="0" Orientation="0" LockTypeChange="N" ' \
			'Type="Free" Float1="0" Float2="0" Float3="0" Int1="0" Int2="0">\n' \
			'  <Name></Name>\n' \
			'  <Value></Value>\n' \
			'  <Pads/>\n' \
			'  <Shapes/>\n' \
			'</Pattern>\n'
		actual = DipTrace.Pattern()
		self.assertEqual(expected, str(actual))

	def test_constructor_2(self):
		expected = \
			'<Pattern RefDes="D" Mounting="None" Width="0" Height="0" Orientation="0" LockTypeChange="N" ' \
			'Type="Free" Float1="0" Float2="0" Float3="0" Int1="0" Int2="0">\n' \
			'  <Name></Name>\n' \
			'  <Value></Value>\n' \
			'  <Pads/>\n' \
			'  <Shapes/>\n' \
			'</Pattern>\n'
		actual = DipTrace.Pattern(
			reference='D',
		)
		self.assertEqual(expected, str(actual))

	def test_constructor_3(self):
		expected = \
			'<Pattern RefDes="D" Mounting="None" Width="0" Height="0" Orientation="0" LockTypeChange="N" ' \
			'Type="Free" Float1="0" Float2="0" Float3="0" Int1="0" Int2="0">\n' \
			'  <Name>Untitled</Name>\n' \
			'  <Value>T1</Value>\n' \
			'  <Origin X="0" Y="0" Cross="Y" Circle="Y" Common="Hide" Courtyard="Show"/>\n' \
			'  <DefPad PadType="PadT0"/>\n' \
			'  <Pads>\n' \
			'    <Pad PadType="PadT0" Enabled="Y" X="0" Y="0" Angle="0" Locked="N" Side="Top">\n' \
			'      <Number>1</Number>\n' \
			'    </Pad>\n' \
			'  </Pads>\n' \
			'  <Shapes>\n' \
			'    <Shape Type="Rectangle" Locked="Y" Layer="Top Silk" AllLayers="N">\n' \
			'      <Points>\n' \
			'        <Item X="-2.54" Y="2.54"/>\n' \
			'        <Item X="2.54" Y="-2.54"/>\n' \
			'      </Points>\n' \
			'    </Shape>\n' \
			'  </Shapes>\n' \
			'  <Dimensions>\n' \
			'    <Dimension Enabled="Y" Locked="Y" Type="Horizontal" '\
			'Connected1="-1" Object1="0" SubObject1="0" Point1="0" ' \
			'Connected2="-1" Object2="0" SubObject2="0" Point2="0" ' \
			'Layer="Top Dimension" X1="0" Y1="0" X2="0" Y2="0" XD="0" YD="0" ' \
			'ArrowSize="0.667" Units="Common" FontVector="Y" FontName="Tahoma" ' \
			'FontSize="2" FontScale="1" FontWidth="-2" ShowUnits="N" Angle="0" ' \
			'ExternalRadius="0" PointerMode="0"/>\n' \
			'  </Dimensions>\n' \
			'  <Model3D Mirror="N" NoSearch="N" Units="Wings" IPC_XOff="0" IPC_YOff="0" ' \
			'AutoHeight="0" AutoColor="4934475" Type="File" KeepPins="N">\n' \
			'    <Rotate X="0" Y="0" Z="0"/>\n' \
			'    <Offset X="0" Y="0" Z="0"/>\n' \
			'    <Zoom X="1" Y="1" Z="1"/>\n' \
			'  </Model3D>\n' \
			'</Pattern>\n'

		actual = DipTrace.Pattern(
			name='Untitled',
			value='T1',
			reference='D',
			default_pad='PadT0',
			pads=[
				DipTrace.Pad(
					type='PadT0'
				)
			],
			origin=DipTrace.Origin(cross=True, circle=True, common=DipTrace.Visible.Hide, courtyard=DipTrace.Visible.Show),
			shapes=[
				DipTrace.Shape(
					enabled=None,
					group=None,
					width=None,
					locked=True,
					all_layers=False,
					type=DipTrace.ShapeType.Rectangle,
					layer=DipTrace.LayerType.TopSilk,
					points=[
						DipTrace.Point(x=-2.54, y=2.54),
						DipTrace.Point(x=2.54, y=-2.54),
					]
				)
			],
			dimensions=[
				DipTrace.Dimension()
			],
			model=DipTrace.Model3D(
				units=DipTrace.Units3D.wings
			)
		)
		self.assertEqual(expected, str(actual))
		self.assertEqual(True, actual.dimensions[0].enabled)
		self.assertEqual(False, actual.pads[0].locked)
		self.assertEqual(True, actual.origin.cross)

		actual.dimensions = None
		self.assertEqual(None, actual.dimensions)

		actual.origin = None
		self.assertEqual(None, actual.origin)
