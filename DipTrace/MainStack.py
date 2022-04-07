#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright 2021-... Oleksandr Kolodkin <alexandr.kolodkin@gmail.com>.
# This program is distributed under the MIT license.
# Glory to Ukraine!

import DipTrace


class MainStack(
	DipTrace.WidthHeightMixin,
	DipTrace.CornerMixin
):
	tag = 'MainStack'
	defaults = {
		'shape': DipTrace.PadShape.Obround,
		**DipTrace.WidthHeightMixin.defaults,
		'x_offset': 0.0,
		'y_offset': 0.0,
		**DipTrace.CornerMixin.defaults
	}

	@property
	def shape(self) -> DipTrace.PadShape:
		return DipTrace.PadShape.from_str(self.root.get('Shape'))

	@shape.setter
	def shape(self, shape: DipTrace.PadShape):
		self.root.attrib['Shape'] = shape.value

	@property
	def x_offset(self) -> float:
		return DipTrace.to_float(self.root.get('XOff'))

	@x_offset.setter
	def x_offset(self, x_offset: float):
		self.root.attrib['XOff'] = DipTrace.from_float(x_offset)

	@property
	def y_offset(self) -> float:
		return DipTrace.to_float(self.root.get('YOff'))

	@y_offset.setter
	def y_offset(self, y_offset: float):
		self.root.attrib['YOff'] = DipTrace.from_float(y_offset)

