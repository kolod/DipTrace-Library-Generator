#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright 2021-... Oleksandr Kolodkin <alexandr.kolodkin@gmail.com>.
# This program is distributed under the MIT license.
# Glory to Ukraine!

from enum import Enum
from typing import Optional

from lxml import etree

import DipTrace


class Part(DipTrace.Common):

	class PartType(Enum):
		Normal = 'Normal'
		Power = 'Power'
		NetPort = 'Net Port'

	class Style(Enum):
		Free = 0
		TwoSides = 1
		ChipTwoSides = 2
		ChipFourSides = 3

	def __init__(self, name: str, ref: str, value: str = '', part_name: str = 'Part 1'):
		super().__init__('Part')
		self.reference_designator = ref
		self.part_type = self.PartType.Normal
		self.show_numbers = 1
		self.style = self.Style.Free
		self.pin_count_1 = 0
		self.pin_count_2 = 0
		self.width = 0.0
		self.height = 0.0
		self.locked = False
		self.index = 1
		self.name = name
		self.part_name = part_name
		self.value = value
		self.origin = DipTrace.Origin()
		self._get_first_or_new('Category')

	@property
	def name(self) -> Optional[str]:
		return self._get_first_text_or_default('Name')

	@name.setter
	def name(self, name: str):
		self._set_first_text('Name', name)

	@property
	def part_name(self) -> Optional[str]:
		return self._get_first_text_or_default('PartName')

	@part_name.setter
	def part_name(self, name: str):
		self._set_first_text('PartName', name)

	@property
	def value(self) -> Optional[str]:
		return self._get_first_text_or_default('Value')

	@value.setter
	def value(self, value: str):
		self._set_first_text('Value', value)

	@property
	def pattern(self) -> Optional[str]:
		return self._get_first_attribute_or_default('Pattern', 'PatternType')

	@pattern.setter
	def pattern(self, value: str):
		self._get_first_or_new('Pattern').attrib['PatternType'] = value

	@property
	def origin(self):
		return DipTrace.Origin().load(self.root.find('Origin'))

	@origin.setter
	def origin(self, origin: DipTrace.Origin):
		self.root.replace(self._get_first_or_new('Origin'), origin.root)

	@property
	def reference_designator(self) -> Optional[str]:
		return self.root.get('RefDes')

	@reference_designator.setter
	def reference_designator(self, value: str):
		self.root.attrib['RefDes'] = value

	@property
	def part_type(self) -> Optional[PartType]:
		return self.root.get('PartType')

	@part_type.setter
	def part_type(self, value: PartType):
		self.root.attrib['PartType'] = value.value

	@property
	def style(self) -> Optional[Style]:
		return self.root.get('Type')

	@style.setter
	def style(self, value: Style):
		self.root.attrib['Type'] = DipTrace.from_int(value.value)

	@property
	def pin_count_1(self) -> int:
		return DipTrace.to_int(self.root.get('Int1'))

	@pin_count_1.setter
	def pin_count_1(self, count: int):
		self.root.attrib['Int1'] = DipTrace.from_int(count)

	@property
	def pin_count_2(self) -> int:
		return DipTrace.to_int(self.root.get('Int2'))

	@pin_count_2.setter
	def pin_count_2(self, count: int):
		self.root.attrib['Int2'] = DipTrace.from_int(count)

	@property
	def width(self) -> float:
		return DipTrace.to_float(self.root.get('Width'))

	@width.setter
	def width(self, width: float):
		self.root.attrib['Width'] = DipTrace.from_float(width)

	@property
	def height(self) -> float:
		return DipTrace.to_int(self.root.get('Height'))

	@height.setter
	def height(self, height: float):
		self.root.attrib['Height'] = DipTrace.from_float(height)

	@property
	def show_numbers(self) -> int:
		return DipTrace.to_int(self.root.get('ShowNumbers'))

	@show_numbers.setter
	def show_numbers(self, state: int):
		self.root.attrib['ShowNumbers'] = DipTrace.from_int(state)

	@property
	def index(self) -> int:
		return DipTrace.to_int(self.root.get('SubFolderIndex'))

	@index.setter
	def index(self, index: int):
		self.root.attrib['SubFolderIndex'] = DipTrace.from_int(index)

	@property
	def locked(self) -> bool:
		return DipTrace.to_bool(self.root.attrib.get('LockTypeChange'))

	@locked.setter
	def locked(self, state: bool):
		self.root.attrib['LockTypeChange'] = DipTrace.from_bool(state)

	def add_pins(self, pins):
		if type(pins) is list:
			for pin in pins:
				self.add_pins(pin)
		elif type(pins) is DipTrace.Pin:
			self._get_first_or_new('Pins').append(pins.root)

	def add_shapes(self, shapes):
		if type(shapes) is list:
			for shape in shapes:
				self.add_shapes(shape)
		elif type(shapes) is DipTrace.Shape:
			self._get_first_or_new('Shapes').append(shapes.root)

	def add_categories(self, categories):
		if type(categories) is list:
			for category in categories:
				self.add_categories(category)
		elif type(categories) is str:
			etree.SubElement(self._get_first_or_new('Category'), 'Name').text = categories


if __name__ == "__main__":
	pass
