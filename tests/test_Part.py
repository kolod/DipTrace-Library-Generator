#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright 2021-... Oleksandr Kolodkin <alexandr.kolodkin@gmail.com>.
# This program is distributed under the MIT license.
# Glory to Ukraine!

import unittest
import DipTrace


class TestPart(unittest.TestCase):
	def test_constructor_1(self):
		expected = \
			'<Part RefDes="D" PartType="Normal" ShowNumbers="1" Type="0" Int1="0" Int2="0" ' \
			'Width="5.08" Height="2.54" LockTypeChange="N" SubFolderIndex="1">\n' \
			'  <Name>SMAJ5.0A</Name>\n' \
			'  <PartName>Part 1</PartName>\n' \
			'  <Value>5 V</Value>\n' \
			'  <Origin X="0" Y="0"/>\n' \
			'  <SpiceModel Type="SubCkt"/>\n' \
			'  <Category/>\n' \
			'  <Pins/>\n' \
			'  <Shapes/>\n' \
			'  <Pattern PatternType=""/>\n' \
			'</Part>\n'

		actual = DipTrace.Part(name='SMAJ5.0A', reference='D', value='5 V')
		actual.width = 5.08
		actual.height = 2.54

		self.assertEqual(expected, str(actual))

	def test_constructor_2(self):
		expected = \
			'<Part RefDes="D" PartType="Normal" ShowNumbers="1" Type="0" Int1="0" Int2="0" ' \
			'Width="5.08" Height="2.54" LockTypeChange="N" SubFolderIndex="1">\n' \
			'  <Name>SMAJ5.0A</Name>\n' \
			'  <PartName>Part 1</PartName>\n' \
			'  <Value>5 V</Value>\n' \
			'  <Origin X="0" Y="0"/>\n' \
			'  <SpiceModel Type="SubCkt"/>\n' \
			'  <Category/>\n' \
			'  <Pins>\n' \
			'    <Pin X="0" Y="0" Enabled="Y" Locked="Y" Type="Default" ElectricType="Undefined" ' \
			'Orientation="0" PadIndex="1" Length="2.54" ShowName="N" NumXShift="0" NumYShift="0" ' \
			'NameXShift="0" NameYShift="0" SignalDelay="0" NumOrientation="0" NameOrientation="0">\n' \
			'      <Name></Name>\n' \
			'      <PadNumber></PadNumber>\n' \
			'      <NameFont Size="5" Width="-2" Scale="1"/>\n' \
			'    </Pin>\n' \
			'  </Pins>\n' \
			'  <Shapes/>\n' \
			'  <Pattern PatternType="PatType0"/>\n' \
			'</Part>\n'

		actual = DipTrace.Part(
			name='SMAJ5.0A',
			reference='D',
			value='5 V',
			pattern='PatType0',
			width=5.08,
			height=2.54,
			pins=[DipTrace.Pin()]
		)

		self.assertEqual(expected, str(actual))
		self.assertEqual('SMAJ5.0A', actual.name)
		self.assertEqual('D', actual.reference)
		self.assertEqual('5 V', actual.value)
		self.assertEqual(5.08, actual.width)
		self.assertEqual(2.54, actual.height)
		self.assertEqual(0.0, actual.origin.x)
		self.assertEqual('Part 1', actual.part_name)
		self.assertEqual('PatType0', actual.pattern)
		self.assertEqual(DipTrace.SpiceModelType.SubCkt, actual.spice_model.model_type)
		self.assertEqual(DipTrace.PartType.Normal, actual.part_type)
		self.assertEqual(0, actual.pin_count[1])

	def test_normalize(self):
		part = DipTrace.Part(
			name='normalize',
			reference='n',
			shapes=[
				DipTrace.Shape(
					points=[
						DipTrace.Point(x=-2.54, y=-1.27),
						DipTrace.Point(x=2.54, y=1.27)
					]
				)
			]
		).normalize()
		expected = 5.08, 2.54
		actual = part.width, part.height
		self.assertEqual(expected, actual)
