#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright 2021-... Oleksandr Kolodkin <alexandr.kolodkin@gmail.com>.
# This program is distributed under the MIT license.
# Glory to Ukraine!

import DipTrace


class SpiceModel(DipTrace.Base):
	tag = 'SpiceModel'
	defaults = {
		'model_type': DipTrace.SpiceModelType.SubCkt,
	}

	@property
	def model_type(self) -> DipTrace.SpiceModelType:
		return DipTrace.SpiceModelType.from_str(self.root.get('Type'))

	@model_type.setter
	def model_type(self, model_type: DipTrace.SpiceModelType):
		self.root.attrib['Type'] = model_type.value
