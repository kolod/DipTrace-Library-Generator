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

		actual = DipTrace.Part(name='SMAJ5.0A', ref='D', value='5 V')
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
			'    <Pin X="0" Y="0" Enabled="Y" Locked="N" Type="Default" ElectricType="Undefined" ' \
			'Orientation="0" PadIndex="1" Length="2.54" ShowName="N" NumXShift="0" NumYShift="0" ' \
			'NameXShift="0" NameYShift="0" SignalDelay="0" NumOrientation="0" NameOrientation="0">\n' \
			'      <Name></Name>\n' \
			'      <PadNumber></PadNumber>\n' \
			'      <NameFont Size="5" Width="-2" Scale="1"/>\n' \
			'    </Pin>\n' \
			'  </Pins>\n' \
			'  <Shapes/>\n' \
			'  <Pattern PatternType=""/>\n' \
			'</Part>\n'

		actual = DipTrace.Part(name='SMAJ5.0A', ref='D', value='5 V')
		actual.width = 5.08
		actual.height = 2.54
		actual.add_pins([DipTrace.Pin()])

		self.assertEqual(expected, str(actual))

	def test_normalize(self):
		part = DipTrace.Part('normalize', 'n').add_shapes([
			DipTrace.Shape().add_points([
				DipTrace.Point(-2.54, -1.27),
				DipTrace.Point(2.54, 1.27)
			])
		])

		print(str(part))

		expected = (5.08, 2.54)
		actual = part.normalize()
		self.assertEqual(expected, actual)
