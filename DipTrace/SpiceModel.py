#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright 2021-... Oleksandr Kolodkin <alexandr.kolodkin@gmail.com>.
# This program is distributed under the MIT license.
# Glory to Ukraine!

from enum import Enum
from lxml import etree
import DipTrace


class SpiceModel(DipTrace.Common):

	class ModelType(Enum):
		SubCkt = 'SubCkt'

	def __init__(self, model_type=ModelType.SubCkt):
		super().__init__('SpiceModel')
		self.model_type = model_type

	@property
	def model_type(self):
		return self.root.get('Type')

	@model_type.setter
	def model_type(self, model_type: ModelType):
		self.root.attrib['Type'] = model_type.value


if __name__ == "__main__":
	pass
