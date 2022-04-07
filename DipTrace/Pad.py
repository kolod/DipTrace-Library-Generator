#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright 2021-... Oleksandr Kolodkin <alexandr.kolodkin@gmail.com>.
# This program is distributed under the MIT license.
# Glory to Ukraine!

import DipTrace
from typing import Optional, List


class Pad(
	DipTrace.PointMixin,
	DipTrace.LockedMixin,
	DipTrace.EnabledMixin,
	DipTrace.GroupMixin,
	DipTrace.AngleMixin
):
	tag = 'Pad'
	defaults = {
		'type': '',
		**DipTrace.EnabledMixin.defaults,
		**DipTrace.PointMixin.defaults,
		**DipTrace.AngleMixin.defaults,
		'group': None,
		'locked': False,
		'side': DipTrace.Side.Top,
		'number': '1',
	}

	@property
	def type(self) -> str:
		return self.root.get('PadType')

	@type.setter
	def type(self, t: str):
		self.root.attrib['PadType'] = t

	@property
	def side(self) -> Optional[DipTrace.Side]:
		return DipTrace.Side.from_str(self.root.get("Side"))

	@side.setter
	def side(self, side: DipTrace.Side):
		self.root.attrib['Side'] = side.value

	@property
	def number(self) -> str:
		return self._get_first_text_or_default('Number', '0')

	@number.setter
	def number(self, value: str):
		self._set_first_text('Number', value)


class PadsMixin(DipTrace.Base):
	pads_tag = 'Pads'
	defaults = {'pads': ()}

	@property
	def pads(self) -> List[Pad]:
		return list(map(lambda x: Pad(x), self._get_all_sub_tags(self.pads_tag, DipTrace.Pad.tag)))

	@pads.setter
	def pads(self, pads: List[Pad]):
		x = self._get_first_or_new(self.pads_tag)
		for pad in pads:
			x.append(pad.root)
