#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright 2021-... Oleksandr Kolodkin <alexandr.kolodkin@gmail.com>.
# This program is distributed under the MIT license.
# Glory to Ukraine!

from typing import Optional
import DipTrace


class Pad(
	DipTrace.PointMixin,
	DipTrace.LockedMixin,
	DipTrace.EnabledMixin,
	DipTrace.GroupMixin,
):
	tag = 'Pad'
	defaults = {
		'side': DipTrace.Side.Top,
		'angle': 0.0,
		'number': 1,
		**DipTrace.PointMixin.defaults,
		**DipTrace.LockedMixin.defaults,
		**DipTrace.EnabledMixin.defaults,
		**DipTrace.GroupMixin.defaults,
	}

	@property
	def side(self) -> Optional[DipTrace.Side]:
		return self.root.get("Side")

	@side.setter
	def side(self, side: DipTrace.Side):
		self.root.attrib['Side'] = side.name

	@property
	def angle(self):
		return self.root.get("Angle")

	@angle.setter
	def angle(self, value: float):
		self.root.attrib['Angle'] = value

	@property
	def number(self) -> str:
		return self._get_first_text_or_default('Number', '0')

	@number.setter
	def number(self, value: str):
		self._set_first_text('Number', value)


if __name__ == "__main__":
	pass
