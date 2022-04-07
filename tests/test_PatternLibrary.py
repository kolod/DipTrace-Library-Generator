#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright 2021-... Oleksandr Kolodkin <alexandr.kolodkin@gmail.com>.
# This program is distributed under the MIT license.
# Glory to Ukraine!


import unittest
import DipTrace


class TestDipTracePatternLibrary(unittest.TestCase):

	def __init__(self, *args, **kwargs):
		self.x = DipTrace.PatternLibrary()
		self.y = DipTrace.PatternLibrary(name='LIB', hint='HINT', units=DipTrace.Units.mil)
		self.z = DipTrace.PatternLibrary()
		self.z.name = 'LIB'
		self.z.hint = 'HINT'
		self.z.units = DipTrace.Units.mil
		self.z.version = '5.0'
		super().__init__(*args, **kwargs)

	def test_constructor(self):
		expected = '<Library Type="DipTrace-PatternLibrary" Name="" Hint="" Version="4.2.0.1" Units="mm"/>\n'
		actual = DipTrace.PatternLibrary()
		self.assertEqual(expected, str(actual))

#	def test_load(self):
#		expected = '<Library Type="DipTrace-PatternLibrary" Version="4.2.0.1" Units="mm" Name="" Hint=""/>\n'
#		actual = DipTrace.PatternLibrary().load('../samples/Diodes TVS.libxml')
#		self.assertEqual(expected, str(actual))

	def test_name(self):
		self.assertEqual('', self.x.name)
		self.assertEqual('LIB', self.y.name)
		self.assertEqual('LIB', self.z.name)

	def test_hint(self):
		self.assertEqual('', self.x.hint)
		self.assertEqual('HINT', self.y.hint)
		self.assertEqual('HINT', self.z.hint)

	def test_version(self):
		self.assertEqual('4.2.0.1', self.x.version)
		self.assertEqual('4.2.0.1', self.y.version)
		self.assertEqual('5.0', self.z.version)

	def test_units(self):
		self.assertEqual(DipTrace.Units.mm, self.x.units)
		self.assertEqual(DipTrace.Units.mil, self.y.units)
		self.assertEqual(DipTrace.Units.mil, self.z.units)
