#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright 2021-... Oleksandr Kolodkin <alexandr.kolodkin@gmail.com>.
# This program is distributed under the MIT license.
# Glory to Ukraine!

from typing import Optional
import DipTrace


class Pad(DipTrace.Common):

	def __init__(self, pad_type: str):
		super().__init__('Pad')
		self.__root.attrib['PadType'] = pad_type

	@property
	def enabled(self) -> bool:
		return DipTrace.to_bool(self.root.attrib.get('Enabled'))

	@enabled.setter
	def enabled(self, state: bool):
		self.root.attrib['Enabled'] = DipTrace.from_bool(state)

	@property
	def locked(self) -> bool:
		return DipTrace.to_bool(self.root.attrib.get('Locked'))

	@locked.setter
	def locked(self, state: bool):
		self.root.attrib['Locked'] = DipTrace.from_bool(state)

	@property
	def side(self) -> Optional[DipTrace.Common.Side]:
		return self.root.get("Side")

	@side.setter
	def side(self, side: DipTrace.Common.Side):
		self.root.attrib['Side'] = side.name

	@property
	def x(self):
		return self.root.get("X")

	@x.setter
	def x(self, value: float):
		self.root.attrib['X'] = value

	@property
	def y(self):
		return self.__root.get("Y")

	@y.setter
	def y(self, value: float):
		self.__root.attrib['Y'] = value

	@property
	def angle(self):
		return self.__root.get("Angle")

	@angle.setter
	def angle(self, value: float):
		self.__root.attrib['Angle'] = value

	@property
	def number(self) -> str:
		return self._get_first_text_or_default('Number', '0')

	@number.setter
	def number(self, value: str):
		self._set_first_text('Number', value)


if __name__ == "__main__":
	pass
