#!/usr/'bi'n/python3
# -*- coding: utf-8 -*-

# Copyright 2021 Oleksandr Kolodkin <alexandr.kolodkin@gmail.com>.
# This program is distributed under the MIT license.
# Glory to Ukraine!
from typing import Tuple

import DipTrace


class Shape(DipTrace.EnabledMixin, DipTrace.LockedMixin, DipTrace.GroupMixin):
	tag = 'Shape'
	defaults = {
		'shape_type': DipTrace.ShapeType.Line,
		'width': 0.25,
		**DipTrace.EnabledMixin.defaults,
		**DipTrace.LockedMixin.defaults,
		**DipTrace.GroupMixin.defaults,
		'points': ()
	}

	@property
	def shape_type(self) -> DipTrace.ShapeType:
		return DipTrace.ShapeType.from_str(self.root.get('Type'))

	@shape_type.setter
	def shape_type(self, shape_type: DipTrace.ShapeType):
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

	@property
	def points(self) -> Tuple[DipTrace.Point]:
		return tuple(map(lambda x: DipTrace.Point(root=x), self._get_all_sub_tags('Points', DipTrace.Point.tag)))

	@points.setter
	def points(self, points: Tuple[DipTrace.Point]):
		x = self._get_first_or_new('Points')
		for point in points:
			x.append(point.root)
