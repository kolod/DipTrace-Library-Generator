#!/usr/'bi'n/python3
# -*- coding: utf-8 -*-

# Copyright 2021 Oleksandr Kolodkin <alexandr.kolodkin@gmail.com>.
# This program is distributed under the MIT license.
# Glory to Ukraine!

from enum import Enum
from typing import List

import DipTrace


class Shape(DipTrace.Common):

	class ShapeType(Enum):
		Line = 'Line'
		Arrow = 'Arrow'
		Arc = 'Arc'
		Rectangle = 'Rectangle'
		FillRect = 'FillRect'
		Obround = 'Obround'
		FillObround = 'FillObround'
		Polyline = 'Polyline'
		Polygon = 'Polygon'
		Text = 'Text'

	def __init__(self, shape_type: ShapeType = ShapeType.Line, width: float = 0.25):
		super().__init__('Shape')
		self.shape_type = shape_type
		self.width = width
		self.enabled = True
		self.locked = True

	@property
	def shape_type(self):
		return self.root.get('Type')

	@shape_type.setter
	def shape_type(self, shape_type: ShapeType):
		self.root.attrib['Type'] = shape_type.value

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
	def width(self) -> float:
		return DipTrace.to_float(self.root.get('LineWidth'))

	@width.setter
	def width(self, width: float):
		self.root.attrib['LineWidth'] = DipTrace.from_float(width)

	def add_points(self, points):
		if type(points) is list:
			for point in points:
				self.add_points(point)
		elif type(points) is DipTrace.Point:
			self._get_first_or_new('Points').append(points.root)
		return self


if __name__ == "__main__":
	pass
