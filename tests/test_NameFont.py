#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright 2021-... Oleksandr Kolodkin <alexandr.kolodkin@gmail.com>.
# This program is distributed under the MIT license.
# Glory to Ukraine!

import unittest
import DipTrace


class TestNameFont(unittest.TestCase):

	def test_constructor_1(self):
		font = DipTrace.NameFont()
		self.assertEqual('<NameFont Size="5" Width="-2" Scale="1"/>\n', str(font))
		self.assertEqual(5, font.size)
		self.assertEqual(-2, font.width)
		self.assertEqual(1, font.scale)

	def test_constructor_2(self):
		font = DipTrace.NameFont(size=10, width=-3, scale=0.8)
		self.assertEqual('<NameFont Size="10" Width="-3" Scale="0.8"/>\n', str(font))
		self.assertEqual(10, font.size)
		self.assertEqual(-3, font.width)
		self.assertEqual(0.8, font.scale)

	def test_constructor_3(self):
		font = DipTrace.NameFont()
		font.size = 10
		font.width = -3
		font.scale = 0.8
		self.assertEqual('<NameFont Size="10" Width="-3" Scale="0.8"/>\n', str(font))
		self.assertEqual(10, font.size)
		self.assertEqual(-3, font.width)
		self.assertEqual(0.8, font.scale)
