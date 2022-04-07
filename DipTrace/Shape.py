#!/usr/'bi'n/python3
# -*- coding: utf-8 -*-

# Copyright 2021 Oleksandr Kolodkin <alexandr.kolodkin@gmail.com>.
# This program is distributed under the MIT license.
# Glory to Ukraine!

import DipTrace
from typing import List, Optional


class Shape(
	DipTrace.EnabledMixin,
	DipTrace.LockedMixin,
	DipTrace.GroupMixin,
	DipTrace.PointsMixin,
	DipTrace.LayerMixin,
):
	tag = 'Shape'
	defaults = {
		'type': DipTrace.ShapeType.Line,
		'width': None,
		'enabled': None,
		**DipTrace.LockedMixin.defaults,
		**DipTrace.GroupMixin.defaults,
		**DipTrace.PointsMixin.defaults,
		'layer': None,
		'all_layers': None,
	}

	@property
	def type(self) -> DipTrace.ShapeType:
		return DipTrace.ShapeType.from_str(self.root.get('Type'))

	@type.setter
	def type(self, shape_type: DipTrace.ShapeType):
		self.root.attrib['Type'] = shape_type.value

	@property
	def width(self) -> Optional[float]:
		if 'LineWidth' in self.root.attrib:
			return DipTrace.to_float(self.root.get('LineWidth'))
		else:
			return None

	@width.setter
	def width(self, width: float):
		if width is not None:
			self.root.attrib['LineWidth'] = DipTrace.from_float(width)
		elif 'LineWidth' in self.root.attrib:
			self.root.attrib.pop('LineWidth')

	@property
	def all_layers(self) -> Optional[bool]:
		if 'AllLayers' in self.root.attrib:
			return DipTrace.to_bool(self.root.get('AllLayers'))
		else:
			return None

	@all_layers.setter
	def all_layers(self, state: Optional[bool]):
		if state is not None:
			self.root.attrib['AllLayers'] = DipTrace.from_bool(state)
		elif 'AllLayers' in self.root.attrib:
			self.root.attrib.pop('AllLayers')


class ShapesMixin(DipTrace.Base):
	defaults = {'shapes': ()}

	@property
	def shapes(self) -> List[Shape]:
		return list(map(lambda x: Shape(x), self._get_all_sub_tags('Shapes', 'Shape')))

	@shapes.setter
	def shapes(self, shapes: List[Shape]):
		x = self._get_first_or_new('Shapes')
		for shape in shapes:
			x.append(shape.root)
