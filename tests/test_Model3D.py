#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright 2021-... Oleksandr Kolodkin <alexandr.kolodkin@gmail.com>.
# This program is distributed under the MIT license.
# Glory to Ukraine!

import unittest
import DipTrace


class TestModel3D(unittest.TestCase):

	def test_model_3d_1(self):
		expected = \
			'<Model3D Mirror="N" NoSearch="N" Units="mm" IPC_XOff="0" IPC_YOff="0" ' \
			'AutoHeight="0" AutoColor="4934475" Type="File" KeepPins="N">\n' \
			'  <Rotate X="0" Y="0" Z="0"/>\n' \
			'  <Offset X="0" Y="0" Z="0"/>\n' \
			'  <Zoom X="1" Y="1" Z="1"/>\n' \
			'</Model3D>\n'
		actual = DipTrace.Model3D(

		)
		self.assertEqual(expected, str(actual))

	def test_model_3d_2(self):
		expected = \
			'<Model3D Mirror="Y" NoSearch="Y" Units="Wings" IPC_XOff="2" IPC_YOff="-0.4" ' \
			'AutoHeight="2.5" AutoColor="16744512" Type="Outline" KeepPins="Y">\n' \
			'  <Filename>\n' \
			'    <Path>WF-02_Stright.wrl</Path>\n' \
			'    <Var>WF-02_Stright.wrl</Var>\n' \
			'  </Filename>\n' \
			'  <Rotate X="1" Y="2" Z="5"/>\n' \
			'  <Offset X="1.5" Y="2.5" Z="5"/>\n' \
			'  <Zoom X="0.005" Y="0.005" Z="0.005"/>\n' \
			'</Model3D>\n'
		actual = DipTrace.Model3D(
			mirror=True,
			no_search=True,
			units=DipTrace.Units3D.wings,
			ipc_x_offset=2,
			ipc_y_offset=-.4,
			height=2.5,
			color=DipTrace.Color(r=64, g=128, b=255),
			type=DipTrace.ModelType.Outline,
			keep_pins=True,
			filename=DipTrace.Filename(
				path='WF-02_Stright.wrl',
				var='WF-02_Stright.wrl'
			),
			rotate=DipTrace.Rotate(x=1.0, y=2.0, z=5),
			offset=DipTrace.Offset(x=1.5, y=2.5, z=5),
			zoom=DipTrace.Zoom(x=0.005, y=0.005, z=0.005),
		)
		self.assertEqual(expected, str(actual))
		self.assertEqual(True, actual.mirror)
		self.assertEqual(True, actual.no_search)
		self.assertEqual(True, actual.keep_pins)
		self.assertEqual(DipTrace.Units3D.wings, actual.units)
		self.assertEqual(2.0, actual.ipc_x_offset)
		self.assertEqual(-.4, actual.ipc_y_offset)
		self.assertEqual(2.5, actual.height)
		self.assertEqual(DipTrace.Color(r=64, g=128, b=255), actual.color)
		self.assertEqual(DipTrace.ModelType.Outline, actual.type)
		self.assertEqual('WF-02_Stright.wrl', actual.filename.path)
		self.assertEqual('WF-02_Stright.wrl', actual.filename.var)
		self.assertEqual(2.0, actual.rotate.y)
		self.assertEqual(1.5, actual.offset.x)
		self.assertEqual(0.005, actual.zoom.z)

		actual.filename = None

		self.assertEqual(None, actual.filename)

	pass
