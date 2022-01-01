#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright 2021-... Oleksandr Kolodkin <alexandr.kolodkin@gmail.com>.
# This program is distributed under the MIT license.
# Glory to Ukraine!

import DipTrace


class PatternLibrary(DipTrace.LibraryMixin):
	defaults = {
		'type': 'DipTrace-PatternLibrary',
		**DipTrace.LibraryMixin.defaults
	}

	def add_pad_types(self, pad_types):
		if type(pad_types) is list:
			for pad_type in pad_types:
				self.add_pad_types(pad_type)
		elif type(pad_types) is DipTrace.PadType:
			self._get_first_or_new('PadTypes').insert(pad_types.root)
		return self


if __name__ == "__main__":
	pass
