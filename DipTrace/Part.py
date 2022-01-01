#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright 2021-... Oleksandr Kolodkin <alexandr.kolodkin@gmail.com>.
# This program is distributed under the MIT license.
# Glory to Ukraine!

from typing import Optional, Tuple
from lxml import etree
import DipTrace


class Part(DipTrace.Base):
	tag = 'Part'
	defaults = {
		'reference': '',
		'part_type': DipTrace.PartType.Normal,
		'show_numbers': 1,
		'style': DipTrace.Style.Free,
		'pin_count_1': 0,
		'pin_count_2': 0,
		'width': 0.0,
		'height': 0.0,
		'locked': False,
		'index': 1,
		'name': '',
		'part_name': 'Part 1',
		'value': '',
		'origin': DipTrace.Origin(),
		'spice_model': DipTrace.SpiceModel(),
		'categories': (),
		'pins': (),
		'shapes': (),
		'pattern': '',
	}

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self._get_first_or_new('Category')
		self._get_first_or_new('Pins')
		self._get_first_or_new('Shapes')

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
	def origin(self) -> DipTrace.Origin:
		return DipTrace.Origin(root=self.root.find('Origin'))

	@origin.setter
	def origin(self, origin: DipTrace.Origin):
		self.root.replace(self._get_first_or_new('Origin'), origin.root)

	@property
	def spice_model(self) -> DipTrace.SpiceModel:
		return DipTrace.SpiceModel(root=self.root.find('SpiceModel'))

	@spice_model.setter
	def spice_model(self, spice_model: DipTrace.SpiceModel):
		self.root.replace(self._get_first_or_new('SpiceModel'), spice_model.root)

	@property
	def reference(self) -> Optional[str]:
		return self.root.get('RefDes')

	@reference.setter
	def reference(self, value: str):
		self.root.attrib['RefDes'] = value

	@property
	def part_type(self) -> Optional[DipTrace.PartType]:
		return self.root.get('PartType')

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
		return DipTrace.to_float(self.root.get('Height'))

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

	@property
	def pins(self) -> Tuple[DipTrace.Pin]:
		return tuple(map(lambda x: DipTrace.Pin(root=x), self._get_all_sub_tags('Pins', DipTrace.Pin.tag)))

	@pins.setter
	def pins(self, pins: Tuple[DipTrace.Pin]):
		x = self._get_first_or_new('Pins')
		for pin in pins:
			x.append(pin.root)

	@property
	def shapes(self) -> Tuple[DipTrace.Shape]:
		return tuple(map(lambda x: DipTrace.Shape(root=x), self._get_all_sub_tags('Shapes', DipTrace.Shape.tag)))

	@shapes.setter
	def shapes(self, shapes: Tuple[DipTrace.Shape]):
		x = self._get_first_or_new('Shapes')
		for shape in shapes:
			x.append(shape.root)

	@property
	def categories(self) -> Tuple[str]:
		return tuple(map(lambda x: str(x.text), self._get_all_sub_tags('Category', 'Name')))

	@categories.setter
	def categories(self, categories: Tuple[str]):
		x = self._get_first_or_new('Category')
		for category in categories:
			etree.SubElement(x, 'Name').text = category

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
		print(f'Normalized size: {width}, {height}')

		self.width = width
		self.height = height
		return self


if __name__ == "__main__":
	pass
