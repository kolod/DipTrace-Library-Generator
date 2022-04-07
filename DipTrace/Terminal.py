#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright 2021-... Oleksandr Kolodkin <alexandr.kolodkin@gmail.com>.
# This program is distributed under the MIT license.
# Glory to Ukraine!

import DipTrace


class Terminal(
	DipTrace.WidthHeightMixin,
	DipTrace.AngleMixin,
	DipTrace.PointMixin,
	DipTrace.PointsMixin,
	DipTrace.CornerMixin
):
	tag = 'Terminal'
	defaults = {
		'shape': DipTrace.TerminalShape.Rectangle,
		**DipTrace.PointMixin.defaults,
		**DipTrace.AngleMixin.defaults,
		**DipTrace.WidthHeightMixin.defaults,
		**DipTrace.PointsMixin.defaults,
		**DipTrace.CornerMixin.defaults
	}

	@property
	def shape(self) -> DipTrace.TerminalShape:
		return DipTrace.TerminalShape.from_str(self.root.get('Shape'))

	@shape.setter
	def shape(self, shape: DipTrace.TerminalShape):
		self.root.attrib['Shape'] = shape.value
