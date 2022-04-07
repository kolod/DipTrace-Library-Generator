#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright 2021-... Oleksandr Kolodkin <alexandr.kolodkin@gmail.com>.
# This program is distributed under the MIT license.
# Glory to Ukraine!

from typing import List
import DipTrace


class PadType(DipTrace.Base):
	tag = 'PadType'
	defaults = {
		'name': '',
		'type': DipTrace.MountType.SurfaceMount,
		'hole_type': DipTrace.HoleType.Obround,
		'hole': 0.0,
		'side': DipTrace.Side.Top,
		'main_stack': DipTrace.MainStack(),
		'terminals': ()
	}

	@property
	def name(self) -> str:
		return self.root.get("Name")

	@name.setter
	def name(self, name: str):
		self.root.attrib['Name'] = name

	@property
	def type(self) -> DipTrace.MountType:
		return DipTrace.MountType.from_str(self.root.get('Type'))

	@type.setter
	def type(self, t: DipTrace.MountType):
		self.root.attrib['Type'] = t.value

	@property
	def hole_type(self) -> DipTrace.HoleType:
		return DipTrace.HoleType.from_str(self.root.get("HoleType"))

	@hole_type.setter
	def hole_type(self, hole_type: DipTrace.HoleType):
		self.root.attrib['HoleType'] = hole_type.value

	@property
	def side(self) -> DipTrace.Side:
		return DipTrace.Side.from_str(self.root.get("Side"))

	@side.setter
	def side(self, side: DipTrace.Side):
		self.root.attrib['Side'] = side.value

	@property
	def hole(self) -> float:
		return DipTrace.to_float(self.root.get("Hole"))

	@hole.setter
	def hole(self, hole: float):
		self.root.attrib['Hole'] = DipTrace.from_float(hole)

	@hole.setter
	def hole(self, hole: float):
		self.root.attrib['Hole'] = str(hole)

	@property
	def main_stack(self) -> DipTrace.MainStack:
		return DipTrace.MainStack(self.root.find('MainStack'))

	@main_stack.setter
	def main_stack(self, stack: DipTrace.MainStack):
		self.root.replace(self._get_first_or_new('MainStack'), stack.root)

	@property
	def terminals(self) -> List[DipTrace.Terminal]:
		def apply(terminal: lxml.etree._Element): # noqa:
			return DipTrace.Terminal(terminal)
		return list(map(apply, self._get_all_sub_tags('Terminals', DipTrace.Terminal.tag)))

	@terminals.setter
	def terminals(self, terminals: List[DipTrace.Terminal]):
		x = self._get_first_or_new('Terminals')
		for terminal in terminals:
			x.append(terminal.root)
