#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright 2021-... Oleksandr Kolodkin <alexandr.kolodkin@gmail.com>.
# This program is distributed under the MIT license.
# Glory to Ukraine!

from typing import Optional, Tuple
import DipTrace
from DipTrace import VisibleType


class Part(
	DipTrace.WidthHeightMixin,
	DipTrace.ReferenceMixin,
	DipTrace.ShapesMixin,
	DipTrace.TypeLockedMixin,
	DipTrace.OriginMixin,
	DipTrace.CategoryMixin
):
	tag = 'Part'
	defaults = {
		**DipTrace.ReferenceMixin.defaults,
		'part_type': DipTrace.PartType.Normal,
		'show_numbers': DipTrace.VisibleType.Common,
		'style': DipTrace.Style.Free,
		'pin_count': (0, 0),
		**DipTrace.WidthHeightMixin.defaults,
		**DipTrace.TypeLockedMixin.defaults,
		'index': 1,
		'name': '',
		'part_name': 'Part 1',
		'value': '',
		**DipTrace.OriginMixin.defaults,
		'spice_model': DipTrace.SpiceModel,
		**DipTrace.CategoryMixin.defaults,
		'pins': (),
		**DipTrace.ShapesMixin.defaults,
		'pattern': '',
	}

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
	def spice_model(self) -> DipTrace.SpiceModel:
		return DipTrace.SpiceModel(self.root.find('SpiceModel'))

	@spice_model.setter
	def spice_model(self, spice_model: DipTrace.SpiceModel):
		self.root.replace(self._get_first_or_new('SpiceModel'), spice_model.root)

	@property
	def part_type(self) -> Optional[DipTrace.PartType]:
		return DipTrace.PartType.from_str(self.root.get('PartType'))

	@part_type.setter
	def part_type(self, part_type: DipTrace.PartType):
		self.root.attrib['PartType'] = part_type.value

	@property
	def style(self) -> Optional[DipTrace.Style]:
		return self.root.get('Type')

	@style.setter
	def style(self, value: DipTrace.Style):
		self.root.attrib['Type'] = DipTrace.from_int(value.value)

	@property
	def pin_count(self) -> Tuple[int, int]:
		return DipTrace.to_int(self.root.get('Int1')), DipTrace.to_int(self.root.get('Int2'))

	@pin_count.setter
	def pin_count(self, count: Tuple[int, int]):
		self.root.attrib['Int1'] = DipTrace.from_int(count[0])
		self.root.attrib['Int2'] = DipTrace.from_int(count[1])

	@property
	def show_numbers(self) -> VisibleType:
		return VisibleType(DipTrace.to_int(self.root.get('ShowNumbers')))

	@show_numbers.setter
	def show_numbers(self, state: VisibleType):
		self.root.attrib['ShowNumbers'] = DipTrace.from_int(state.value)

	@property
	def index(self) -> int:
		return DipTrace.to_int(self.root.get('SubFolderIndex'))

	@index.setter
	def index(self, index: int):
		self.root.attrib['SubFolderIndex'] = DipTrace.from_int(index)

	@property
	def pins(self) -> Tuple[DipTrace.Pin]:
		return tuple(map(lambda x: DipTrace.Pin(x), self._get_all_sub_tags('Pins', DipTrace.Pin.tag)))

	@pins.setter
	def pins(self, pins: Tuple[DipTrace.Pin]):
		x = self._get_first_or_new('Pins')
		for pin in pins:
			x.append(pin.root)

	def normalize(self):

		# Find limits
		min_x: float = float('Inf')
		max_x: float = float('-Inf')
		min_y: float = float('Inf')
		max_y: float = float('-Inf')

		for shape_tag in self.root.findall('.//Shapes/Shape'):
			if shape_tag.get('Type') == DipTrace.ShapeType.Arc.value:
				pass

			else:
				for point_tag in shape_tag.findall('.//Points/Item'):
					if (x := float(point_tag.get('X'))) is not None:
						if (y := float(point_tag.get('Y'))) is not None:
							if x > max_x:
								max_x = x
							if x < min_x:
								min_x = x
							if y > max_y:
								max_y = y
							if y < min_y:
								min_y = y

		width = max_x - min_x
		height = max_y - min_y

		if (width > float('-inf')) and (height > float('-inf')):
			self.width = width
			self.height = height

		return self
