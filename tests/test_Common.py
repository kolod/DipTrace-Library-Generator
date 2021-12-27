#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright 2021-... Oleksandr Kolodkin <alexandr.kolodkin@gmail.com>.
# This program is distributed under the MIT license.
# Glory to Ukraine!

import unittest
import DipTrace


class TestCommon(unittest.TestCase):
	def test_to_int(self):
		self.assertEqual(123, DipTrace.to_int('123'))
		self.assertEqual(-123, DipTrace.to_int('-123'))
		self.assertEqual(0, DipTrace.to_int('-12.3'))
		self.assertEqual(-1, DipTrace.to_int('-1.23', -1))

	def test_from_int(self):
		self.assertEqual('123', DipTrace.from_int(123))
		self.assertEqual('-123', DipTrace.from_int(-123))

	def test_to_float(self):
		self.assertEqual(12.3, DipTrace.to_float('12.3'))
		self.assertEqual(-12.3, DipTrace.to_float('-12.3'))
		self.assertEqual(0.0, DipTrace.to_float('-1.2.3'))
		self.assertEqual(1.0, DipTrace.to_float('-1.2.3', 1.0))
		self.assertEqual(0.6065, DipTrace.to_float('0.6065'))

	def test_from_flot(self):
		self.assertEqual('123', DipTrace.from_float(123))
		self.assertEqual('12.3', DipTrace.from_float(12.3))
		self.assertEqual('0.6065', DipTrace.from_float(0.6065))

	def test_to_bool(self):
		self.assertEqual(True, DipTrace.to_bool('Y'))
		self.assertEqual(False, DipTrace.to_bool('N'))
		self.assertEqual(False, DipTrace.to_bool('y'))
		self.assertEqual(False, DipTrace.to_bool(''))
		self.assertEqual(False, DipTrace.to_bool('YY'))

	def test_from_bool(self):
		self.assertEqual('Y', DipTrace.from_bool(True))
		self.assertEqual('N', DipTrace.from_bool(False))


if __name__ == '__main__':
	unittest.main()
