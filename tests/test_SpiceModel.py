#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright 2021-... Oleksandr Kolodkin <alexandr.kolodkin@gmail.com>.
# This program is distributed under the MIT license.
# Glory to Ukraine!

import unittest
import DipTrace


class TestSpiceModel(unittest.TestCase):

	def test_constructor_1(self):
		expected = '<SpiceModel Type="SubCkt"/>\n'
		actual = DipTrace.SpiceModel()
		self.assertEqual(expected, str(actual))
		self.assertEqual(DipTrace.SpiceModelType.SubCkt, actual.model_type)

	def test_constructor_2(self):
		expected = '<SpiceModel Type="SubCkt"/>\n'
		actual = DipTrace.SpiceModel(
			model_type=DipTrace.SpiceModelType.SubCkt
		)
		self.assertEqual(expected, str(actual))
		self.assertEqual(DipTrace.SpiceModelType.SubCkt, actual.model_type)
