#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright 2021-... Oleksandr Kolodkin <alexandr.kolodkin@gmail.com>.
# This program is distributed under the MIT license.
# Glory to Ukraine!

import lxml.etree
import DipTrace
from typing import Tuple, List, Optional


class Connection:
	connected: int
	root_object: int
	sub_object: int
	point: int

	def __init__(self, connected: int = -1, root_object: int = 0, sub_object: int = 0, point: int = 0):
		self.connected = connected
		if connected >= 0:
			self.root_object = root_object
			self.sub_object = sub_object
			self.point = point
		else:
			self.root_object = 0
			self.sub_object = 0
			self.point = 0

	def __str__(self) -> str:
		return f'(Connected={self.connected}, Object={self.root_object}, SubObject={self.sub_object}, Point={self.point})'

	def __eq__(self, other) -> bool:
		return \
			(self.connected == other.connected) and \
			(self.root_object == other.root_object) and \
			(self.sub_object == other.sub_object) and \
			(self.point == other.point)

	@classmethod
	def from_tag(cls, tag: lxml.etree._Element, index: int): # noqa:
		return Connection(
			connected=DipTrace.to_int(tag.get(f'Connected{index}')),
			root_object=DipTrace.to_int(tag.get(f'Object{index}')),
			sub_object=DipTrace.to_int(tag.get(f'SubObject{index}')),
			point=DipTrace.to_int(tag.get(f'Point{index}')),
		)

	def to_tag(self, tag: lxml.etree._Element, index: int): # noqa:
		tag.attrib[f'Connected{index}'] = DipTrace.from_int(self.connected)
		tag.attrib[f'Object{index}'] = DipTrace.from_int(self.root_object)
		tag.attrib[f'SubObject{index}'] = DipTrace.from_int(self.sub_object)
		tag.attrib[f'Point{index}'] = DipTrace.from_int(self.point)


class Dimension(
	DipTrace.EnabledMixin,
	DipTrace.LockedMixin,
	DipTrace.LayerMixin,
	DipTrace.AngleMixin,
):
	tag = 'Dimension'
	defaults = {
		**DipTrace.EnabledMixin.defaults,
		**DipTrace.LockedMixin.defaults,
		'type': DipTrace.DimensionType.Horizontal,
		'connection_1': Connection(),
		'connection_2': Connection(),
		'layer': DipTrace.LayerType.TopDimension,
		'point_1': DipTrace.Point(),
		'point_2': DipTrace.Point(),
		'point_d': DipTrace.Point(),
		'arrow_size': 0.667,
		'units': DipTrace.DimensionUnits.common,
		'font': (True, 'Tahoma', 2, 1.0, -2.0, False),
		**DipTrace.AngleMixin.defaults,
		'radius': 0.0,
		'pointer_mode': 0,
		'text': None
	}

	@property
	def type(self) -> DipTrace.DimensionType:
		return DipTrace.DimensionType.from_str(self.root.get('Type'))

	@type.setter
	def type(self, t: DipTrace.DimensionType):
		self.root.attrib['Type'] = t.value

	@property
	def connection_1(self) -> Connection:
		return Connection.from_tag(self.root, 1)

	@connection_1.setter
	def connection_1(self, connection: Connection):
		connection.to_tag(self.root, 1)

	@property
	def connection_2(self) -> Connection:
		return Connection.from_tag(self.root, 2)

	@connection_2.setter
	def connection_2(self, connection: Connection):
		connection.to_tag(self.root, 2)

	@property
	def units(self) -> DipTrace.DimensionUnits:
		return DipTrace.DimensionUnits.from_str(self.root.get("Units"))

	@units.setter
	def units(self, units: DipTrace.DimensionUnits):
		self.root.attrib['Units'] = units.value

	@property
	def point_1(self) -> DipTrace.Point:
		return DipTrace.Point(
			x=DipTrace.to_float(self.root.get('X1')),
			y=DipTrace.to_float(self.root.get('Y1'))
		)

	@point_1.setter
	def point_1(self, point: DipTrace.Point):
		self.root.attrib['X1'] = DipTrace.from_float(point.x)
		self.root.attrib['Y1'] = DipTrace.from_float(point.y)

	@property
	def point_2(self) -> DipTrace.Point:
		return DipTrace.Point(
			x=DipTrace.to_float(self.root.get('X2')),
			y=DipTrace.to_float(self.root.get('Y2'))
		)

	@point_2.setter
	def point_2(self, point: DipTrace.Point):
		self.root.attrib['X2'] = DipTrace.from_float(point.x)
		self.root.attrib['Y2'] = DipTrace.from_float(point.y)

	@property
	def point_d(self) -> DipTrace.Point:
		return DipTrace.Point(
			x=DipTrace.to_float(self.root.get('XD')),
			y=DipTrace.to_float(self.root.get('YD'))
		)

	@point_d.setter
	def point_d(self, point: DipTrace.Point):
		self.root.attrib['XD'] = DipTrace.from_float(point.x)
		self.root.attrib['YD'] = DipTrace.from_float(point.y)

	@property
	def arrow_size(self) -> float:
		return DipTrace.to_float(self.root.get('ArrowSize'))

	@arrow_size.setter
	def arrow_size(self, size: float):
		self.root.attrib['ArrowSize'] = DipTrace.from_float(size)

	@property
	def font(self) -> Tuple[bool, str, int, float, float, bool]:
		return (
			DipTrace.to_bool(self.root.get("FontVector")),
			self.root.get("FontName"),
			DipTrace.to_int(self.root.get("FontSize")),
			DipTrace.to_float(self.root.get("FontScale")),
			DipTrace.to_float(self.root.get("FontWidth")),
			DipTrace.to_bool(self.root.get("ShowUnits")),
		)

	@font.setter
	def font(self, vector: Tuple[bool, str, int, float, float, bool]):
		self.root.attrib['FontVector'] = DipTrace.from_bool(vector[0])
		self.root.attrib['FontName'] = vector[1]
		self.root.attrib['FontSize'] = DipTrace.from_int(vector[2])
		self.root.attrib['FontScale'] = DipTrace.from_float(vector[3])
		self.root.attrib['FontWidth'] = DipTrace.from_float(vector[4])
		self.root.attrib['ShowUnits'] = DipTrace.from_bool(vector[5])

	@property
	def radius(self) -> float:
		return DipTrace.to_float(self.root.get('ExternalRadius'))

	@radius.setter
	def radius(self, radius: float):
		self.root.attrib['ExternalRadius'] = DipTrace.from_float(radius)

	@property
	def pointer_mode(self) -> int:
		return DipTrace.to_int(self.root.get('PointerMode'))

	@pointer_mode.setter
	def pointer_mode(self, pointer_mode: int):
		self.root.attrib['PointerMode'] = DipTrace.from_int(pointer_mode)

	@property
	def text(self) -> Optional[str]:
		if (x := self.root.find('PointerText')) is not None:
			return x.text
		else:
			return None

	@text.setter
	def text(self, text: Optional[str]):
		if text is not None:
			self._set_first_text('PointerText', text)
		elif (x := self.root.find('PointerText')) is not None:
			self.root.remove(x)

	def normalize(self):
		if (self.pointer_mode == 0) or (self.text == ''):
			for child in list(self.root):
				self.root.remove(child)


class DimensionsMixin(DipTrace.Base):
	defaults = {'dimensions': None}

	@property
	def dimensions(self) -> Optional[List[Dimension]]:
		if (x := self.root.find('Dimensions')) is not None:
			return list(map(lambda x: Dimension(x), x))
		else:
			return None

	@dimensions.setter
	def dimensions(self, dimensions: Optional[List[Dimension]]):
		if dimensions is not None:
			x = self._get_first_or_new('Dimensions')
			for dimension in dimensions:
				x.append(dimension.root)
		elif (x := self.root.find('Dimensions')) is not None:
			self.root.remove(x)
