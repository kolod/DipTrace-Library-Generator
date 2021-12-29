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
			'<Pin X="0" Y="0" Enabled="Y" Locked="N" Type="Default" ElectricType="Undefined" Orientation="0" PadIndex="1" '\
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

		actual = DipTrace.Pin(x=-6.35, y=-8.89)
		actual.name = '12'
		actual.number = 12
		actual.enabled = True
		actual.locked = False
		actual.pin_type = DipTrace.Pin.PinType.Shift
		actual.electric_type = DipTrace.Pin.ElectricType.Undefined
		actual.font = DipTrace.NameFont(5, -2)
		actual.orientation = 0.0
		actual.pad_index = 12
		actual.length = 3.81
		actual.show_name = False
		actual.number_x_shift = 0
		actual.number_y_shift = 0
		actual.name_x_shift = 0.6065
		actual.name_y_shift = -1.2851
		actual.signal_delay = 1
		actual.number_orientation = 0
		actual.name_orientation = 0

		self.assertEqual(expected, str(actual))
