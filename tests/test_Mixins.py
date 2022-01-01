#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright 2021-... Oleksandr Kolodkin <alexandr.kolodkin@gmail.com>.
# This program is distributed under the MIT license.
# Glory to Ukraine!

import unittest
import DipTrace


class Test(DipTrace.Base):
	tag = 'Part'


class TestBase(unittest.TestCase):
	def test_constructor(self):
		expected = '<Part/>\n'
		actual = Test()
		self.assertEqual(expected, str(actual))

	def test_load(self):
		expected = \
			'<Part RefDes="n" PartType="Normal" ShowNumbers="1" Type="0" Int1="0" Int2="0" Width="0" Height="0" ' \
			'LockTypeChange="N" SubFolderIndex="1">\n' \
			'  <Name>normalize</Name>\n' \
			'  <PartName>Part 1</PartName>\n' \
			'  <Value/>\n' \
			'  <Origin X="0" Y="0"/>\n' \
			'  <SpiceModel Type="SubCkt"/>\n' \
			'  <Category/>\n' \
			'  <Pins/>\n' \
			'  <Shapes>\n' \
			'    <Shape Type="Line" LineWidth="0.25" Enabled="Y" Locked="Y">\n' \
			'      <Points>\n' \
			'        <Item X="-2.54" Y="-1.27"/>\n' \
			'        <Item X="2.54" Y="1.27"/>\n' \
			'      </Points>\n' \
			'    </Shape>\n' \
			'  </Shapes>\n' \
			'  <Pattern PatternType=""/>\n' \
			'</Part>\n'
		actual = Test().load('../samples/part_test.sample.xml')
		self.assertEqual(expected, str(actual))
