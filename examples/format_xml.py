#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright 2021-... Oleksandr Kolodkin <alexandr.kolodkin@gmail.com>.
# This program is distributed under the MIT license.
# Glory to Ukraine!


from lxml import etree


def format_xml(filename: str):
	with open(filename, encoding='utf-8', mode='r+') as datafile:
		datafile.readline()
		data = '<?xml version="1.0" encoding="utf-8"?>\n' + \
			etree.tostring(etree.fromstring(datafile.read()), encoding='utf-8', pretty_print=True).decode('utf-8')
		datafile.seek(0)
		datafile.write(data)
		datafile.truncate()
		datafile.close()


if __name__ == "__main__":
	format_xml('../tvs.xml')
