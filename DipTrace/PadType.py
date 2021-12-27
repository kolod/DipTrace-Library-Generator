#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright 2021-... Oleksandr Kolodkin <alexandr.kolodkin@gmail.com>.
# This program is distributed under the MIT license.
# Glory to Ukraine!

from lxml import etree
from typing import Optional
from enum import Enum
import DipTrace


class PadType(DipTrace.Common):
	class HoleType(Enum):
		Round = 'Round'
		Obround = 'Obround'

	class Shape(Enum):
		Ellipse = 'Ellipse'
		Obround = 'Obround'
		Rectangle = 'Rectangle'
		Polygon = 'Polygon'
		DShape = 'D-shape'

	def __init__(self, name: str = ''):
		super().__init__('PadType')
		self.__root.attrib['Name'] = name

	@property
	def name(self) -> Optional[str]:
		return self.__root.get("Name")

	@name.setter
	def name(self, name: str):
		self.__root.attrib['Name'] = name

	@property
	def hole_type(self) -> Optional[HoleType]:
		value = self.__root.get("HoleType")
		return self.HoleType[value]

	@hole_type.setter
	def hole_type(self, hole_type: HoleType):
		self.__root.attrib['HoleType'] = hole_type.name

	@property
	def side(self) -> Optional[DipTrace.Common.Side]:
		return self.__root.get("Side")

	@side.setter
	def side(self, side: DipTrace.Common.Side):
		self.__root.attrib['Side'] = side.name

	@property
	def hole(self) -> Optional[float]:
		try:
			return float(self.__root.get("Hole"))
		except ValueError:
			return None

	def add_main_stack(self, shape: Shape, width: float, height: float, x_offset: float, y_offset: float, points):
		main_stack = etree.Element('MainStack')
		main_stack.attrib['Shape'] = shape
		main_stack.attrib['Width'] = width
		main_stack.attrib['Height'] = height
		main_stack.attrib['XOff'] = x_offset
		main_stack.attrib['YOff'] = y_offset
		if shape == self.Shape.Polygon:
			points_element = etree.SubElement(self.root, 'Points')
			for point in points:
				points_element.insert(point.root)

		self.__root.insert(main_stack)

	@hole.setter
	def hole(self, hole: float):
		self.__root.attrib['Hole'] = str(hole)

	def __str__(self) -> str:
		return etree.tostring(self.__root, encoding='utf-8', pretty_print=True).decode('utf-8')


if __name__ == "__main__":
	pass
