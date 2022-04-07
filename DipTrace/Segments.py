#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright 2021-... Oleksandr Kolodkin <alexandr.kolodkin@gmail.com>.
# This program is distributed under the MIT license.
# Glory to Ukraine!

import DipTrace
from typing import List, Optional


class Segment(DipTrace.Base):
	tag = 'Item'
	defaults = {
		'x1': 0.0,
		'y1': 0.0,
		'x2': 0.0,
		'y2': 0.0,
	}

	@property
	def x1(self) -> float:
		return DipTrace.to_float(self.root.get('X1'))

	@x1.setter
	def x1(self, x: float):
		self.root.attrib['X1'] = DipTrace.from_float(x)

	@property
	def y1(self) -> float:
		return DipTrace.to_float(self.root.get('Y1'))

	@y1.setter
	def y1(self, y: float):
		self.root.attrib['Y1'] = DipTrace.from_float(y)

	@property
	def x2(self) -> float:
		return DipTrace.to_float(self.root.get('X2'))

	@x2.setter
	def x2(self, x: float):
		self.root.attrib['X2'] = DipTrace.from_float(x)

	@property
	def y2(self) -> float:
		return DipTrace.to_float(self.root.get('Y2'))

	@y2.setter
	def y2(self, y: float):
		self.root.attrib['Y2'] = DipTrace.from_float(y)


class TopSegmentsMixin(DipTrace.Base):
	defaults = {'top_segments': None}

	@property
	def top_segments(self) -> List[Segment]:
		return list(map(lambda v: Segment(v), self._get_all_sub_tags('TopSegments', 'Item')))

	@top_segments.setter
	def top_segments(self, segments: Optional[List[Segment]]):
		if segments is not None:
			x = self._get_first_or_new('TopSegments')
			for segment in segments:
				x.append(segment.root)
		else:
			if (x := self.root.find('TopSegments')) is not None:
				self.root.remove(x)


class BottomSegmentsMixin(DipTrace.Base):
	defaults = {'bottom_segments': None}

	@property
	def bottom_segments(self) -> List[Segment]:
		return list(map(lambda v: Segment(v), self._get_all_sub_tags('BotSegments', 'Item')))

	@bottom_segments.setter
	def bottom_segments(self, segments: Optional[List[Segment]]):
		if segments is not None:
			x = self._get_first_or_new('BotSegments')
			for segment in segments:
				x.append(segment.root)
		else:
			if (x := self.root.find('BotSegments')) is not None:
				self.root.remove(x)
