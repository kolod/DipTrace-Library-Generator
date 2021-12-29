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
		self.y = DipTrace.PatternLibrary(name='LIB', hint='HINT', units='mil')
		self.z = DipTrace.PatternLibrary()
		self.z.name = 'LIB'
		self.z.hint = 'HINT'
		self.z.units = 'mil'
		self.z.version = '5.0'
		super().__init__(*args, **kwargs)

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
		self.assertEqual('mm', self.x.units)
		self.assertEqual('mil', self.y.units)
		self.assertEqual('mil', self.z.units)
