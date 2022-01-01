#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright 2021-... Oleksandr Kolodkin <alexandr.kolodkin@gmail.com>.
# This program is distributed under the MIT license.
# Glory to Ukraine!

import unittest
import DipTrace


class Test(unittest.TestCase):
	def test_format(self):
		expected_filename = '../samples/part_test.sample.xml'
		actual_filename = '../samples/format_test.sample.xml'

		with open(expected_filename, 'r', encoding='utf-8') as expected_file:
			with open(actual_filename, 'w', encoding='utf-8') as actual_file:
				for line in expected_file.readlines():
					actual_file.write(line.strip() + '\n')
				actual_file.flush()
				actual_file.close()
			expected_file.close()

		DipTrace.format_xml(actual_filename)

		with open(expected_filename, 'r', encoding='utf-8') as expected_file:
			with open(actual_filename, 'r', encoding='utf-8') as actual_file:
				expected = expected_file.read()
				actual = actual_file.read()
				self.assertEqual(expected, actual)
