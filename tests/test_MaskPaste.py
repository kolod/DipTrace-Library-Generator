#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright 2021-... Oleksandr Kolodkin <alexandr.kolodkin@gmail.com>.
# This program is distributed under the MIT license.
# Glory to Ukraine!

import unittest
import DipTrace


class TestMaskPaste(unittest.TestCase):

	def test_constructor_1(self):
		expected = '<MaskPaste/>\n'
		actual = DipTrace.MaskPaste()
		self.assertEqual(expected, str(actual))

	def test_constructor_2(self):
		expected = '<MaskPaste TopMask="Open" BotMask="Tented" TopPaste="No Solder" BotPaste="Solder"/>\n'
		actual = DipTrace.MaskPaste(
			top_mask=DipTrace.MaskType.Open,
			bottom_mask=DipTrace.MaskType.Tented,
			top_paste=DipTrace.PasteType.NoSolder,
			bottom_paste=DipTrace.PasteType.Solder
		)
		self.assertEqual(expected, str(actual))

	def test_constructor_3(self):
		expected = \
			'<MaskPaste TopMask="Open" BotMask="Tented" TopPaste="No Solder" BotPaste="Solder" ' \
			'CustomSwell="0.05" CustomShrink="0.1"/>\n'
		actual = DipTrace.MaskPaste(
			top_mask=DipTrace.MaskType.Open,
			bottom_mask=DipTrace.MaskType.Tented,
			top_paste=DipTrace.PasteType.NoSolder,
			bottom_paste=DipTrace.PasteType.Solder,
			swell=0.05,
			shrink=0.1
		)
		self.assertEqual(expected, str(actual))
		self.assertEqual(DipTrace.MaskType.Open, actual.top_mask)
		self.assertEqual(DipTrace.MaskType.Tented, actual.bottom_mask)
		self.assertEqual(DipTrace.PasteType.NoSolder, actual.top_paste)
		self.assertEqual(DipTrace.PasteType.Solder, actual.bottom_paste)
		self.assertEqual(0.05, actual.swell)
		self.assertEqual(0.1, actual.shrink)

		actual.top_mask = DipTrace.MaskType.Common
		actual.top_paste = None
		actual.bottom_mask = DipTrace.PasteType.Common
		actual.bottom_paste = None
		actual.swell = None
		actual.shrink = None

		self.assertEqual('<MaskPaste/>\n', str(actual))

	def test_constructor_4(self):
		expected = \
			'<MaskPaste TopMask="By Paste" BotMask="By Paste" TopPaste="Segments" ' \
			'BotPaste="Segments" Segment_Percent="50" Segment_EdgeGap="0.3" Segment_Gap="0.2" Segment_Side="1">\n' \
			'  <TopSegments>\n' \
			'    <Item X1="-0.53" Y1="0.53" X2="0.53" Y2="-0.53"/>\n' \
			'  </TopSegments>\n' \
			'  <BotSegments>\n' \
			'    <Item X1="-0.53" Y1="0.53" X2="0.53" Y2="-0.53"/>\n' \
			'  </BotSegments>\n' \
			'</MaskPaste>\n'
		actual = DipTrace.MaskPaste(
			top_mask=DipTrace.MaskType.ByPaste,
			bottom_mask=DipTrace.MaskType.ByPaste,
			top_paste=DipTrace.PasteType.Segments,
			bottom_paste=DipTrace.PasteType.Segments,
			segments=(50, 0.3, 0.2, 1),
			top_segments=(DipTrace.Segment(x1=-0.53, y1=0.53, x2=0.53, y2=-0.53),),
			bottom_segments=(DipTrace.Segment(x1=-0.53, y1=0.53, x2=0.53, y2=-0.53),)
		)
		self.assertEqual(expected, str(actual))
		self.assertTupleEqual((50, 0.3, 0.2, 1), actual.segments)

		actual.segments = None
		self.assertEqual(None, actual.segments)

