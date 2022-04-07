#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright 2021-... Oleksandr Kolodkin <alexandr.kolodkin@gmail.com>.
# This program is distributed under the MIT license.
# Glory to Ukraine!

import os
import DipTrace


if __name__ == "__main__":
	for file in os.listdir("source"):
		if file.endswith("xml"):
			DipTrace.format_xml(f"source/{file}")
