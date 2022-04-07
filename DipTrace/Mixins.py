#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright 2021-... Oleksandr Kolodkin <alexandr.kolodkin@gmail.com>.
# This program is distributed under the MIT license.
# Glory to Ukraine!

from typing import Optional
import DipTrace


class GroupMixin(DipTrace.Base):
	defaults = {'group': None}

	@property
	def group(self) -> Optional[int]:
		if 'Group' in self.root.attrib:
			return DipTrace.to_int(self.root.get('Group'))
		else:
			return None

	@group.setter
	def group(self, group: Optional[int]):
		if group is not None:
			self.root.attrib['Group'] = DipTrace.from_int(group)
		elif 'Group' in self.root.attrib:
			self.root.attrib.pop('Group')


class OrientationMixin(DipTrace.Base):
	defaults = {'orientation': 0.0}

	@property
	def orientation(self) -> float:
		return DipTrace.to_float(self.root.get('Orientation'))

	@orientation.setter
	def orientation(self, value: float):
		self.root.attrib['Orientation'] = DipTrace.from_float(value)


class PointMixin(DipTrace.Base):
	defaults = {'x': 0.0, 'y': 0.0}

	@property
	def x(self) -> float:
		return DipTrace.to_float(self.root.get('X'))

	@x.setter
	def x(self, x: float):
		self.root.attrib['X'] = DipTrace.from_float(x)

	@property
	def y(self) -> float:
		return DipTrace.to_float(self.root.get('Y'))

	@y.setter
	def y(self, y: float):
		self.root.attrib['Y'] = DipTrace.from_float(y)


class EnabledMixin(DipTrace.Base):
	defaults = {'enabled': True}

	@property
	def enabled(self) -> Optional[bool]:
		if 'Enabled' in self.root.attrib:
			return DipTrace.to_bool(self.root.attrib.get('Enabled'))
		else:
			return None

	@enabled.setter
	def enabled(self, state: Optional[bool]):
		if state is not None:
			self.root.attrib['Enabled'] = DipTrace.from_bool(state)
		elif 'Enabled' in self.root.attrib:
			self.root.attrib.pop('Enabled')


class LockedMixin(DipTrace.Base):
	defaults = {'locked': True}

	@property
	def locked(self) -> bool:
		return DipTrace.to_bool(self.root.attrib.get('Locked'))

	@locked.setter
	def locked(self, state: bool):
		self.root.attrib['Locked'] = DipTrace.from_bool(state)


class LayerMixin(DipTrace.Base):
	defaults = {'layer': DipTrace.LayerType.TopSilk}

	@property
	def layer(self) -> Optional[DipTrace.LayerType]:
		if 'Layer' in self.root.attrib:
			return DipTrace.LayerType.from_str(self.root.attrib.get('Layer'))
		else:
			return None

	@layer.setter
	def layer(self, layer: Optional[DipTrace.LayerType]):
		if layer is not None:
			self.root.attrib['Layer'] = layer.value
		elif 'Layer' in self.root.attrib:
			self.root.attrib.pop('Layer')


class TypeLockedMixin(DipTrace.Base):
	defaults = {'type_locked': False}

	@property
	def type_locked(self) -> bool:
		return DipTrace.to_bool(self.root.attrib.get('LockTypeChange'))

	@type_locked.setter
	def type_locked(self, state: bool):
		self.root.attrib['LockTypeChange'] = DipTrace.from_bool(state)


class LibraryMixin(DipTrace.Base):
	tag = 'Library'
	defaults = {
		'version': '4.2.0.1',
		'units': DipTrace.Units.mm,
		'name': '',
		'hint': '',
	}

	@property
	def type(self):
		return self.root.get("Type")

	@type.setter
	def type(self, value):
		self.root.attrib['Type'] = value

	@property
	def name(self) -> Optional[str]:
		return self.root.get("Name")

	@name.setter
	def name(self, name: str):
		self.root.attrib['Name'] = name

	@property
	def hint(self) -> Optional[str]:
		return self.root.get("Hint")

	@hint.setter
	def hint(self, hint: str):
		self.root.attrib['Hint'] = hint

	@property
	def version(self) -> Optional[str]:
		return self.root.get("Version")

	@version.setter
	def version(self, version: str):
		self.root.attrib['Version'] = version

	@property
	def units(self) -> DipTrace.Units:
		return DipTrace.Units.from_str(self.root.get("Units"))

	@units.setter
	def units(self, units: DipTrace.Units):
		self.root.attrib['Units'] = units.value


class WidthHeightMixin(DipTrace.Base):
	defaults = {'width': 0.0, 'height': 0.0}

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


class ReferenceMixin(DipTrace.Base):
	defaults = {'reference': ''}

	@property
	def reference(self) -> str:
		return self.root.get('RefDes')

	@reference.setter
	def reference(self, value: str):
		self.root.attrib['RefDes'] = value


class AngleMixin(DipTrace.Base):
	defaults = {'angle': 0.0}

	@property
	def angle(self) -> float:
		return DipTrace.to_float(self.root.get('Angle'))

	@angle.setter
	def angle(self, angle: float):
		self.root.attrib['Angle'] = DipTrace.from_float(angle)


class CornerMixin(DipTrace.Base):
	defaults = {'corner': None}

	@property
	def corner(self) -> Optional[int]:
		if 'Corner' in self.root.attrib:
			return DipTrace.to_int(self.root.get('Corner'))
		else:
			return None

	@corner.setter
	def corner(self, corner: Optional[int]):
		if corner is not None:
			self.root.attrib['Corner'] = DipTrace.from_int(corner)
		elif 'Corner' in self.root.attrib:
			self.root.attrib.pop('Corner')


class CategoryMixin(DipTrace.Base):
	defaults = {'category': DipTrace.Category}

	@property
	def category(self) -> DipTrace.Category:
		return DipTrace.Category(self.root.find('Category'))

	@category.setter
	def category(self, category: DipTrace.Category):
		self.root.replace(self._get_first_or_new('Category'), category.root)
