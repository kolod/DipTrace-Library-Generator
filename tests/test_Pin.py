#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright 2021-... Oleksandr Kolodkin <alexandr.kolodkin@gmail.com>.
# This program is distributed under the MIT license.
# Glory to Ukraine!

import unittest
import DipTrace


class TestPin(unittest.TestCase):
	def test_default_constructor(self):
		expected = \
			'<Pin X="0" Y="0" Enabled="Y" Locked="Y" Type="Default" ElectricType="Undefined" Orientation="0" PadIndex="1" '\
			'Length="2.54" ShowName="N" NumXShift="0" NumYShift="0" NameXShift="0" NameYShift="0" SignalDelay="0" '\
			'NumOrientation="0" NameOrientation="0">\n'\
			'  <Name></Name>\n'\
			'  <PadNumber></PadNumber>\n'\
			'  <NameFont Size="5" Width="-2" Scale="1"/>\n'\
			'</Pin>\n'\

		actual = DipTrace.Pin()

		self.assertEqual(expected, str(actual))

	def test_constructor(self):
		expected = \
			'<Pin X="-6.35" Y="-8.89" Enabled="Y" Locked="N" Type="Shift" ElectricType="Undefined" Orientation="0" ' \
			'PadIndex="12" Length="3.81" ShowName="N" NumXShift="0" NumYShift="0" NameXShift="0.6065" NameYShift="-1.2851" ' \
			'SignalDelay="3" NumOrientation="0" NameOrientation="0">\n' \
			'  <Name>12</Name>\n' \
			'  <PadNumber>12</PadNumber>\n' \
			'  <NameFont Size="5" Width="-2" Scale="1"/>\n' \
			'</Pin>\n'

		actual = DipTrace.Pin(
			x=-6.35, 
			y=-8.89,
			name='12',
			number=12,
			enabled=True,
			locked=False,
			pin_type=DipTrace.PinType.Shift,
			electric_type=DipTrace.ElectricType.Undefined,
			font=DipTrace.NameFont(size=5, width=-2),
			orientation=0.0,
			pad_index=12,
			length=3.81,
			show_name=False,
			number_x_shift=0,
			number_y_shift=0,
			name_x_shift=0.6065,
			name_y_shift=-1.2851,
			signal_delay=1,
			number_orientation=0,
			name_orientation=0,
		)

		self.assertEqual(expected, str(actual))
		self.assertEqual(-6.35, actual.x)
		self.assertEqual(-8.89, actual.y)
		self.assertEqual('12', actual.name)
		self.assertEqual('12', actual.number)
		self.assertEqual(True, actual.enabled)
		self.assertEqual(False, actual.locked)
		self.assertEqual(DipTrace.PinType.Shift, actual.pin_type)
		self.assertEqual(DipTrace.ElectricType.Undefined, actual.electric_type)
		self.assertEqual(0.0, actual.orientation)
		self.assertEqual(12, actual.pad_index)
		self.assertEqual(3.81, actual.length)
		self.assertEqual(False, actual.show_name)
		self.assertEqual(0, actual.number_x_shift)
		self.assertEqual(0, actual.number_y_shift)
		self.assertEqual(0.6065, actual.name_x_shift)
		self.assertEqual(-1.2851, actual.name_y_shift)
		self.assertEqual(1, actual.signal_delay)
		self.assertEqual(0, actual.number_orientation)
		self.assertEqual(0, actual.name_orientation)
		self.assertEqual(str(DipTrace.NameFont(size=5, width=-2)), str(actual.font))
