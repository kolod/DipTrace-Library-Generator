#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright 2021-... Oleksandr Kolodkin <alexandr.kolodkin@gmail.com>.
# This program is distributed under the MIT license.
# Glory to Ukraine!

import DipTrace
from typing import Optional, List


class Component(DipTrace.Base):
	tag = 'Component'
	defaults = {
		'parts': []
	}

	@property
	def parts(self) -> Optional[List[DipTrace.Part]]:
		if len(x := self.root.findall('Part')) > 0:
			return list(map(lambda v: DipTrace.Part(v), x))
		else:
			return None

	@parts.setter
	def parts(self, parts: Optional[List[DipTrace.Part]]):
		if parts is not None:
			for part in parts:
				self.root.append(part.normalize().root)
		else:
			for x in self.root.findall('Part'):
				self.root.remove(x)
