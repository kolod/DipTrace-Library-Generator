#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright 2021-... Oleksandr Kolodkin <alexandr.kolodkin@gmail.com>.
# This program is distributed under the MIT license.
# Glory to Ukraine!

from typing import Optional
import DipTrace


class Color:
	r: int
	g: int
	b: int

	def __init__(self, r: int = 0, g: int = 0, b: int = 0):
		self.r = r
		self.g = g
		self.b = b

	def __eq__(self, other) -> bool:
		return (self.r == other.r) and (self.g == other.g) and (self.b == other.b)

	def __str__(self) -> str:
		return str(self.r + self.g * 256 + self.b * 256 * 256)

	@classmethod
	def from_str(cls, string: str):
		val = DipTrace.to_int(string)
		return Color(
			r=val % 256,
			g=(val // 256) % 256,
			b=val // (256 * 256)
		)


class Model3D(DipTrace.Base):
	tag = 'Model3D'
	defaults = {
		'mirror': False,
		'no_search': False,
		'units': DipTrace.Units3D.mm,
		'ipc_x_offset': 0.0,
		'ipc_y_offset': 0.0,
		'height': 0.0,
		'color': Color(75, 75, 75),
		'type': DipTrace.ModelType.File,
		'keep_pins': False,
		'filename': None,
		'rotate': DipTrace.Rotate(),
		'offset': DipTrace.Offset(),
		'zoom': DipTrace.Zoom(),
	}

	@property
	def mirror(self) -> bool:
		return DipTrace.to_bool(self.root.get("Mirror"))

	@mirror.setter
	def mirror(self, mirror: bool):
		self.root.attrib['Mirror'] = DipTrace.from_bool(mirror)

	@property
	def no_search(self) -> bool:
		return DipTrace.to_bool(self.root.get("NoSearch"))

	@no_search.setter
	def no_search(self, mirror: bool):
		self.root.attrib['NoSearch'] = DipTrace.from_bool(mirror)

	@property
	def units(self) -> DipTrace.Units3D:
		return DipTrace.Units3D.from_str(self.root.get("Units"))

	@units.setter
	def units(self, units: DipTrace.Units3D):
		self.root.attrib['Units'] = units.value

	@property
	def ipc_x_offset(self) -> float:
		return DipTrace.to_float(self.root.get('IPC_XOff'))

	@ipc_x_offset.setter
	def ipc_x_offset(self, offset: float):
		self.root.attrib['IPC_XOff'] = DipTrace.from_float(offset)

	@property
	def ipc_y_offset(self) -> float:
		return DipTrace.to_float(self.root.get('IPC_YOff'))

	@ipc_y_offset.setter
	def ipc_y_offset(self, offset: float):
		self.root.attrib['IPC_YOff'] = DipTrace.from_float(offset)

	@property
	def height(self) -> float:
		return DipTrace.to_float(self.root.get('AutoHeight'))

	@height.setter
	def height(self, offset: float):
		self.root.attrib['AutoHeight'] = DipTrace.from_float(offset)

	@property
	def color(self) -> Color:
		return Color.from_str(self.root.get('AutoColor'))

	@color.setter
	def color(self, color: Color):
		self.root.attrib['AutoColor'] = str(color)

	@property
	def type(self) -> DipTrace.ModelType:
		return DipTrace.ModelType.from_str(self.root.get('Type'))

	@type.setter
	def type(self, t: DipTrace.MountType):
		self.root.attrib['Type'] = t.value

	@property
	def keep_pins(self) -> bool:
		return DipTrace.to_bool(self.root.get("KeepPins"))

	@keep_pins.setter
	def keep_pins(self, mirror: bool):
		self.root.attrib['KeepPins'] = DipTrace.from_bool(mirror)

	@property
	def rotate(self) -> DipTrace.Rotate:
		return DipTrace.Rotate(self.root.find(DipTrace.Rotate.tag))

	@rotate.setter
	def rotate(self, rotate: DipTrace.Rotate):
		self.root.replace(self._get_first_or_new(DipTrace.Rotate.tag), rotate.root)

	@property
	def offset(self) -> DipTrace.Offset:
		return DipTrace.Offset(self.root.find(DipTrace.Offset.tag))

	@offset.setter
	def offset(self, offset: DipTrace.Rotate):
		self.root.replace(self._get_first_or_new(DipTrace.Offset.tag), offset.root)

	@property
	def zoom(self) -> DipTrace.Zoom:
		return DipTrace.Zoom(self.root.find(DipTrace.Zoom.tag))

	@zoom.setter
	def zoom(self, zoom: DipTrace.Rotate):
		self.root.replace(self._get_first_or_new(DipTrace.Zoom.tag), zoom.root)

	@property
	def filename(self) -> Optional[DipTrace.Filename]:
		if (x := self.root.find('Filename')) is not None:
			return DipTrace.Filename(x)
		else:
			return None

	@filename.setter
	def filename(self, filename: Optional[DipTrace.Filename]):
		if filename is not None:
			self.root.replace(self._get_first_or_new('Filename'), filename.root)
		elif (x := self.root.find('Filename')) is not None:
			self.root.remove(x)
