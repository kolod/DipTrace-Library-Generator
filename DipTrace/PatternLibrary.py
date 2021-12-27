#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright 2021-... Oleksandr Kolodkin <alexandr.kolodkin@gmail.com>.
# This program is distributed under the MIT license.
# Glory to Ukraine!

from typing import Optional
import DipTrace


class PatternLibrary(DipTrace.Common):

	def __init__(self, name: str = '', hint: str = '', units: str = 'mm'):
		super().__init__("Library")
		self.root.attrib['Type'] = 'DipTrace-PatternLibrary'
		self.root.attrib['Version'] = '4.2.0.1'
		self.root.attrib['Name'] = name
		self.root.attrib['Hint'] = hint
		self.root.attrib['Units'] = units

	@property
	def type(self):
		return self.root.get("Type")

	@property
	def name(self) -> Optional[str]:
		return self.root.get("Name")

	@name.setter
	def name(self, name: str):
		self.root.attrib['Name'] = name

	@property
	def hint(self) -> Optional[str]:
		return self.root.get("Hint")

	@hint.setter
	def hint(self, hint: str):
		self.root.attrib['Hint'] = hint

	@property
	def version(self) -> Optional[str]:
		return self.root.get("Version")

	@version.setter
	def version(self, version: str):
		self.root.attrib['Version'] = version

	@property
	def units(self) -> Optional[str]:
		return self.root.get("Units")

	@units.setter
	def units(self, units: str):
		self.root.attrib['Units'] = units

	def add_pad_types(self, pad_types):
		if type(pad_types) is list:
			for pad_type in pad_types:
				self.add_pad_types(pad_type)
		elif type(pad_types) is DipTrace.PadType:
			self._get_first_or_new('PadTypes').insert(pad_types.root)

	def save(self, filename: str):
		with open(filename, 'w', encoding='utf-8') as datafile:
			datafile.write(f'<?xml version="1.0" encoding="utf-8"?>\n{self}')


if __name__ == "__main__":
	pass
