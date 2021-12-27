#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright 2021-... Oleksandr Kolodkin <alexandr.kolodkin@gmail.com>.
# This program is distributed under the MIT license.
# Glory to Ukraine!

import unittest
import DipTrace


class TestNameFont(unittest.TestCase):

	def test_constructor(self):
		self.assertEqual('<NameFont Size="5" Width="-2" Scale="1"/>\n', str(DipTrace.NameFont()))
		self.assertEqual('<NameFont Size="10" Width="-3" Scale="0.8"/>\n', str(DipTrace.NameFont(10, -3, 0.8)))


if __name__ == '__main__':
	unittest.main()
