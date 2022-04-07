#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright 2021-... Oleksandr Kolodkin <alexandr.kolodkin@gmail.com>.
# This program is distributed under the MIT license.
# Glory to Ukraine!

import unittest
import DipTrace


class TestPadType(unittest.TestCase):

	def test_constructor_1(self):
		expected = \
			'<PadType Name="" Type="Surface" HoleType="Obround" Hole="0.0" Side="Top">\n' \
			'  <MainStack Shape="Obround" Width="0" Height="0" XOff="0" YOff="0"/>\n' \
			'  <Terminals/>\n' \
			'</PadType>\n'
		actual = DipTrace.PadType()
		self.assertEqual(expected, str(actual))

	def test_constructor_2(self):
		expected = \
			'<PadType Name="PadT0" Type="Through" HoleType="Round" Hole="1.2" Side="Top">\n' \
			'  <MainStack Shape="Obround" Width="1.8" Height="3" XOff="0" YOff="0"/>\n' \
			'  <Terminals>\n' \
			'    <Terminal Shape="Rectangle" X="0" Y="0" Angle="0" Width="0.64" Height="0.64"/>\n' \
			'  </Terminals>\n' \
			'</PadType>\n'
		actual = DipTrace.PadType(
			name='PadT0',
			type=DipTrace.MountType.ThroughHole,
			hole_type=DipTrace.HoleType.Round,
			hole=1.2,
			main_stack=DipTrace.MainStack(
				shape=DipTrace.PadShape.Obround,
				width=1.8,
				height=3.0
			),
			terminals=(DipTrace.Terminal(
				shape=DipTrace.TerminalShape.Rectangle,
				width=0.64,
				height=0.64
			),)
		)
		self.assertEqual(expected, str(actual))
