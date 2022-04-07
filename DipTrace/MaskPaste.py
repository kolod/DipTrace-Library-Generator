#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright 2021-... Oleksandr Kolodkin <alexandr.kolodkin@gmail.com>.
# This program is distributed under the MIT license.
# Glory to Ukraine!

import DipTrace
from typing import Optional, Tuple


class MaskPaste(
	DipTrace.TopSegmentsMixin,
	DipTrace.BottomSegmentsMixin,
):
	tag = 'MaskPaste'
	defaults = {
		'top_mask': DipTrace.MaskType.Common,
		'bottom_mask': DipTrace.MaskType.Common,
		'top_paste': DipTrace.PasteType.Common,
		'bottom_paste': DipTrace.PasteType.Common,
		'swell': None,
		'shrink': None,
		'segments': None,
		**DipTrace.TopSegmentsMixin.defaults,
		**DipTrace.BottomSegmentsMixin.defaults,
	}

	@property
	def top_mask(self) -> DipTrace.MaskType:
		return DipTrace.MaskType.from_str(self.root.get('TopMask'))

	@top_mask.setter
	def top_mask(self, mask: Optional[DipTrace.MaskType]):
		if (mask is not None) and (mask.value is not None):
			self.root.attrib['TopMask'] = mask.value
		elif 'TopMask' in self.root.attrib:
			self.root.attrib.pop('TopMask')

	@property
	def bottom_mask(self) -> DipTrace.MaskType:
		return DipTrace.MaskType.from_str(self.root.get('BotMask'))

	@bottom_mask.setter
	def bottom_mask(self, mask: Optional[DipTrace.MaskType]):
		if (mask is not None) and (mask.value is not None):
			self.root.attrib['BotMask'] = mask.value
		elif 'BotMask' in self.root.attrib:
			self.root.attrib.pop('BotMask')

	@property
	def top_paste(self) -> DipTrace.PasteType:
		return DipTrace.PasteType.from_str(self.root.get('TopPaste'))

	@top_paste.setter
	def top_paste(self, paste: Optional[DipTrace.PasteType]):
		if (paste is not None) and (paste.value is not None):
			self.root.attrib['TopPaste'] = paste.value
		elif 'TopPaste' in self.root.attrib:
			self.root.attrib.pop('TopPaste')

	@property
	def bottom_paste(self) -> DipTrace.PasteType:
		return DipTrace.PasteType.from_str(self.root.get('BotPaste'))

	@bottom_paste.setter
	def bottom_paste(self, paste: Optional[DipTrace.PasteType]):
		if (paste is not None) and (paste.value is not None):
			self.root.attrib['BotPaste'] = paste.value
		elif 'BotPaste' in self.root.attrib:
			self.root.attrib.pop('BotPaste')

	@property
	def swell(self) -> float:
		return DipTrace.to_float(self.root.get('CustomSwell'))

	@swell.setter
	def swell(self, swell: Optional[float]):
		if swell is not None:
			self.root.attrib['CustomSwell'] = DipTrace.from_float(swell)
		elif 'CustomSwell' in self.root.attrib:
			self.root.attrib.pop('CustomSwell')

	@property
	def shrink(self) -> float:
		return DipTrace.to_float(self.root.get('CustomShrink'))

	@shrink.setter
	def shrink(self, shrink: float):
		if shrink is not None:
			self.root.attrib['CustomShrink'] = DipTrace.from_float(shrink)
		elif 'CustomShrink' in self.root.attrib:
			self.root.attrib.pop('CustomShrink')

	@property
	def segments(self) -> Optional[Tuple[float, float, float, int]]:
		if 'Segment_Percent' in self.root.attrib:
			return (
				DipTrace.to_float(self.root.get('Segment_Percent')),
				DipTrace.to_float(self.root.get('Segment_EdgeGap')),
				DipTrace.to_float(self.root.get('Segment_Gap')),
				DipTrace.to_int(self.root.get('Segment_Side')),
			)
		else:
			return None

	@segments.setter
	def segments(self, segments: Optional[Tuple[float, float, float, int]]):
		if segments is not None:
			self.root.attrib['Segment_Percent'] = DipTrace.from_float(segments[0])
			self.root.attrib['Segment_EdgeGap'] = DipTrace.from_float(segments[1])
			self.root.attrib['Segment_Gap'] = DipTrace.from_float(segments[2])
			self.root.attrib['Segment_Side'] = DipTrace.from_int(segments[3])
		else:
			if 'Segment_Percent' in self.root.attrib:
				self.root.attrib.pop('Segment_Percent')
			if 'Segment_EdgeGap' in self.root.attrib:
				self.root.attrib.pop('Segment_EdgeGap')
			if 'Segment_Gap' in self.root.attrib:
				self.root.attrib.pop('Segment_Gap')
			if 'Segment_Side' in self.root.attrib:
				self.root.attrib.pop('Segment_Side')
