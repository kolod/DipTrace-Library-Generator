#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright 2021-... Oleksandr Kolodkin <alexandr.kolodkin@gmail.com>.
# This program is distributed under the MIT license.
# Glory to Ukraine!

import DipTrace


class NameFont(DipTrace.Base):
	tag = 'NameFont'
	defaults = {
		'size': 5,
		'width': -2,
		'scale': 1.0,
	}

	@property
	def size(self) -> int:
		return DipTrace.to_int(self.root.get('Size'))

	@size.setter
	def size(self, size: int):
		self.root.attrib['Size'] = DipTrace.from_int(size)

	@property
	def width(self) -> int:
		return DipTrace.to_int(self.root.get('Width'))

	@width.setter
	def width(self, width: int):
		self.root.attrib['Width'] = DipTrace.from_int(width)

	@property
	def scale(self) -> float:
		return DipTrace.to_float(self.root.get('Scale'))

	@scale.setter
	def scale(self, scale: float):
		self.root.attrib['Scale'] = DipTrace.from_float(scale)
