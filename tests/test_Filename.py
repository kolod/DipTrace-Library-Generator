#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright 2021-... Oleksandr Kolodkin <alexandr.kolodkin@gmail.com>.
# This program is distributed under the MIT license.
# Glory to Ukraine!

import unittest
import DipTrace


class TestFilename(unittest.TestCase):

	def test_filename_1(self):
		expected = \
			'<Filename>\n' \
			'  <Path></Path>\n' \
			'  <Var></Var>\n' \
			'</Filename>\n'
		actual = DipTrace.Filename()
		self.assertEqual(expected, str(actual))
		self.assertEqual('', actual.path)
		self.assertEqual('', actual.var)

	def test_filename_2(self):
		expected = \
			'<Filename>\n' \
			'  <Path>WF-02_Stright.wrl</Path>\n' \
			'  <Var>WF-02_Stright.wrl</Var>\n' \
			'</Filename>\n'
		actual = DipTrace.Filename(
			path='WF-02_Stright.wrl',
			var='WF-02_Stright.wrl'
		)
		self.assertEqual(expected, str(actual))
		self.assertEqual('WF-02_Stright.wrl', actual.path)
		self.assertEqual('WF-02_Stright.wrl', actual.var)
