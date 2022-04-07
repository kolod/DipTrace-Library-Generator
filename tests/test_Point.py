#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright 2021-... Oleksandr Kolodkin <alexandr.kolodkin@gmail.com>.
# This program is distributed under the MIT license.
# Glory to Ukraine!

import unittest
import DipTrace


class TestPoint(unittest.TestCase):

	def test_point_1(self):
		x = DipTrace.Point()
		self.assertEqual('<Item X="0" Y="0"/>\n', str(x))

	def test_point_2(self):
		y = DipTrace.Point(x=10.0, y=20.0)
		self.assertEqual('<Item X="10" Y="20"/>\n', str(y))

	def test_point_3(self):
		z = DipTrace.Point()
		z.x = 10.5
		z.y = 20.5
		self.assertEqual('<Item X="10.5" Y="20.5"/>\n', str(z))

	def test_get_arc_from_points_1(self):
		self.assertEqual(None, DipTrace.get_arc_from_points([
			DipTrace.Point(x=-1.0, y=1.0),
			DipTrace.Point(x=0.0, y=0.0),
			DipTrace.Point(x=1.0, y=-1.0),
		]))

	def test_get_arc_from_points_2(self):
		self.assertEqual(None, DipTrace.get_arc_from_points([
			DipTrace.Point(x=-1.0, y=1.0),
			DipTrace.Point(x=-1.0, y=1.0),
			DipTrace.Point(x=-1.0, y=1.0),
		]))

	def test_get_arc_from_points_3(self):
		self.assertEqual(None, DipTrace.get_arc_from_points([
			DipTrace.Point(x=-1.0, y=1.0),
			DipTrace.Point(x=-1.0, y=1.0),
			DipTrace.Point(x=-1.0, y=1.0),
			DipTrace.Point(x=-1.0, y=1.0),
		]))

	def test_get_arc_from_points_4(self):
		self.assertEqual(None, DipTrace.get_arc_from_points([
			DipTrace.Point(x=-1.0, y=1.0)
		]))

	def test_get_arc_from_points_5(self):
		expected = (4.5, 4.5, 3.5355, -98.1301, -171.8699)
		actual = DipTrace.get_arc_from_points([
			DipTrace.Point(x=4.0, y=1.0),
			DipTrace.Point(x=2.0, y=2.0),
			DipTrace.Point(x=1.0, y=4.0)
		])
		for i in range(len(expected)):
			self.assertAlmostEqual(expected[i], actual[i], delta=0.001)

	def test_get_arc_from_points_6(self):
		expected = (4.5, 4.5, 3.5355, -98.1301, -171.8699)
		actual = DipTrace.get_arc_from_points([
			DipTrace.Point(x=1.0, y=4.0),
			DipTrace.Point(x=2.0, y=2.0),
			DipTrace.Point(x=4.0, y=1.0),
		])
		for i in range(len(expected)):
			self.assertAlmostEqual(expected[i], actual[i], delta=0.001)
