#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright 2021-... Oleksandr Kolodkin <alexandr.kolodkin@gmail.com>.
# This program is distributed under the MIT license.
# Glory to Ukraine!

import DipTrace


class Pattern(DipTrace.Base):

	def __init__(self):
		super().__init__("Pattern")

	@property
	def name(self) -> str:
		return self._get_first_text_or_default('Name')

	@name.setter
	def name(self, value: str):
		self._set_first_text('Name', value)

	@property
	def default_pad_type(self) -> str:
		return self._get_first_attribute_or_default('DefPad', 'PadType')

	@default_pad_type.setter
	def default_pad_type(self, name: str):
		self._get_first_or_new('DefPad').attrib['PadType'] = name

	def add_pads(self, pads):
		if type(pads) is list:
			for pad in pads:
				self.add_pads(pad)
		elif type(pads) is DipTrace.Pad:
			self._get_first_or_new('Pads').insert(pads.root)


if __name__ == "__main__":
	pass
