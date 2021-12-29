#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright 2021-... Oleksandr Kolodkin <alexandr.kolodkin@gmail.com>.
# This program is distributed under the MIT license.
# Glory to Ukraine!

from lxml import etree
import DipTrace


class NameFont(DipTrace.Common):
	def __init__(self, size: int = 5, width: int = -2, scale: float = 1.0):
		super().__init__('NameFont')
		self.root.attrib['Size'] = DipTrace.from_int(size)
		self.root.attrib['Width'] = DipTrace.from_int(width)
		self.root.attrib['Scale'] = DipTrace.from_float(scale)

	@property
	def size(self):
		return self.root.get('Size')

	@size.setter
	def size(self, size: int):
		self.root.attrib['Size'] = str(size)

	@property
	def width(self):
		return self.root.get('Width')

	@width.setter
	def width(self, width: int):
		self.root.attrib['Width'] = str(width)

	@property
	def scale(self):
		return self.root.get('Scale')

	@scale.setter
	def scale(self, scale: float):
		self.root.attrib['Scale'] = str(scale)


if __name__ == "__main__":
	pass
