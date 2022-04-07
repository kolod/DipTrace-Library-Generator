#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright 2021-... Oleksandr Kolodkin <alexandr.kolodkin@gmail.com>.
# This program is distributed under the MIT license.
# Glory to Ukraine!

import DipTrace
from typing import Optional, List
from termcolor import colored


class PatternLibrary(DipTrace.LibraryMixin):
	extensions = ['libxml', 'xml', 'elixml']
	defaults = {
		'type': 'DipTrace-PatternLibrary',
		'name': '',
		'hint': '',
		'version': '4.2.0.1',
		'units': DipTrace.Units.mm,
		'pad_types': None,
		'patterns': None,
	}

	@property
	def pad_types(self) -> Optional[List[DipTrace.PadType]]:
		if (x := self.root.find('PadTypes')) is not None:
			return list(map(lambda v: DipTrace.PadType(v), x.findall('PadType')))
		else:
			return None

	@pad_types.setter
	def pad_types(self, pad_types: Optional[List[DipTrace.PadType]]):
		if pad_types is not None:
			x = self._get_first_or_new('PadTypes')
			for pad_type in pad_types:
				x.append(pad_type.root)
		elif (x := self.root.find('PadTypes')) is not None:
			self.root.remove(x)

	@property
	def patterns(self) -> Optional[List[DipTrace.Pattern]]:
		if (x := self.root.find('Patterns')) is not None:
			return list(map(lambda v: DipTrace.Pattern(v), x.findall('Pattern')))
		else:
			return None

	@patterns.setter
	def patterns(self, patterns: Optional[List[DipTrace.Pattern]]):
		if patterns is not None:
			x = self._get_first_or_new('Patterns')
			for pattern in patterns:
				x.append(pattern.root)
		elif (x := self.root.find('Patterns')) is not None:
			self.root.remove(x)

	def standalone(self):
		print(colored('standalone', 'yellow'))

		old_attrib = dict(self.root.attrib)
		self.root.attrib.clear()

		# Copy type attribute
		if 'Type' in old_attrib:
			self.root.attrib['Type'] = old_attrib['Type']

		# Copy data from hidden fild
		for x in ('Name', 'Hint'):
			if f'Library{x}' in self.hidden:
				self.root.attrib[x] = self.hidden[f'Library{x}']

		# Copy data from old attributes if no hidden data stored
		for x in ('Name', 'Hint'):
			if x not in self.root.attrib:
				if x in old_attrib:
					self.root.attrib[x] = old_attrib[x]

		# Copy other attributes
		for x in ('Version', 'Units'):
			if x in old_attrib:
				self.root.attrib[x] = old_attrib[x]

		# Remove the pattern numbers
		for pattern in self._get_all_sub_tags('Patterns', 'Pattern'):
			if pattern.attrib.get('PatternType', None) is not None:
				del pattern.attrib['PatternType']

			# Remove Group=0
			if (pads := pattern.find('Pads')) is not None:
				for pad in pads.findall('Pad'):
					if pad.attrib.get('Group', None) == "0":
						del pad.attrib['Group']

		return self

	def embedded(self):
		print(colored('embedded', 'yellow'))

		# Move Name & Hint to the hidden fields
		for x in ('Name', 'Hint'):
			if x in self.root.attrib:
				self.hidden[f'Library{x}'] = self.root.attrib[x]
				del self.root.attrib[x]

		# Initialize hidden properties
		if 'parts' not in self.hidden:
			self.hidden['parts'] = dict()

		# Enumerate patterns in the library
		index = 0
		for pattern in self._get_all_sub_tags('Patterns', 'Pattern'):
			old_attrib = dict(pattern.attrib)
			pattern.attrib.clear()
			pattern.attrib['PatternType'] = f'PatType{index}'

			for key, value in old_attrib.items():
				pattern.attrib[key] = value

			# Add Group=0
			for pad in pattern.xpath('Pads/Pad'):
				pad.attrib['Group'] = "0"

			index += 1

		return self

	def normalize(self):
		print(colored('normalize', 'yellow'))

		pad_types = {}
		if self.pad_types is not None:
			for pad_type in self.pad_types:
				if pad_type.name not in pad_types:
					pad_types[pad_type.name] = pad_type

		if self.patterns is not None:
			for pattern in self.patterns:

				# Find limits
				min_x: float = float('Inf')
				max_x: float = float('-Inf')
				min_y: float = float('Inf')
				max_y: float = float('-Inf')

				for pad in pattern.pads:
					if isinstance(pad_type := pad_types.get(pad.type), DipTrace.PadType):
						min_x = min(min_x, pad.x - pad_type.main_stack.width / 2)
						max_x = max(max_x, pad.x + pad_type.main_stack.width / 2)
						min_y = min(min_y, pad.y - pad_type.main_stack.height / 2)
						max_y = max(max_y, pad.y + pad_type.main_stack.height / 2)

				for shape in pattern.shapes:
					if shape.type == DipTrace.ShapeType.Arc:
						center_x, center_y, radius, start_angle, stop_angle = DipTrace.get_arc_from_points(shape.points)
						if center_x is not None:

							for point in shape.points:
								max_x = max(max_x, point.x)
								max_y = max(max_y, point.y)
								min_x = min(min_x, point.x)
								min_y = min(min_y, point.y)

							if DipTrace.is_angle_cross_arc(-180, start_angle, stop_angle):
								min_x = min(min_x, center_x - radius)
							if DipTrace.is_angle_cross_arc(-90, start_angle, stop_angle):
								max_y = max(max_y, center_y + radius)
							if DipTrace.is_angle_cross_arc(0, start_angle, stop_angle):
								max_x = max(max_x, center_x + radius)
							if DipTrace.is_angle_cross_arc(90, start_angle, stop_angle):
								min_y = min(min_y, center_y - radius)
							if DipTrace.is_angle_cross_arc(180, start_angle, stop_angle):
								min_x = min(min_x, center_x - radius)

					else:
						for point in shape.points:
							max_x = max(max_x, point.x)
							max_y = max(max_y, point.y)
							min_x = min(min_x, point.x)
							min_y = min(min_y, point.y)

				width = max_x - min_x
				height = max_y - min_y

				pattern.width = max(0.0, width)
				pattern.height = max(0.0, height)

		return self
