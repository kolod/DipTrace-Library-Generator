#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright 2021-... Oleksandr Kolodkin <alexandr.kolodkin@gmail.com>.
# This program is distributed under the MIT license.
# Glory to Ukraine!
import math

import DipTrace
from typing import Optional, List, Tuple


class Point(DipTrace.PointMixin):
	tag = 'Item'


class Point3D(DipTrace.PointMixin):
	defaults = {
		**DipTrace.PointMixin.defaults,
		'z': 0.0
	}

	@property
	def z(self) -> float:
		return DipTrace.to_float(self.root.get('Z'))

	@z.setter
	def z(self, z: float):
		self.root.attrib['Z'] = DipTrace.from_float(z)


class Rotate(Point3D):
	tag = 'Rotate'
	defaults = {**Point3D.defaults}


class Offset(Point3D):
	tag = 'Offset'
	defaults = {**Point3D.defaults}


class Zoom(Point3D):
	tag = 'Zoom'
	defaults = {
		'x': 1.0,
		'y': 1.0,
		'z': 1.0,
	}


class PointsMixin(DipTrace.Base):
	defaults = {'points': None}

	@property
	def points(self) -> Optional[List[Point]]:
		if (x := self.root.find('Points')) is not None:
			return list(map(lambda v: DipTrace.Point(v), x.findall('Item')))
		else:
			return None

	@points.setter
	def points(self, points: Optional[List[Point]]):
		if points is not None:
			x = self._get_first_or_new('Points')
			for point in points:
				x.append(point.root)
		elif (x := self.root.find('Points')) is not None:
			self.root.remove(x)


def is_angle_cross_arc(angle: float, alpha: float, omega: float) -> bool:
	if omega < alpha:
		result: bool = (angle >= omega) and (angle <= alpha)
	else:
		result: bool = (angle >= omega) or (angle <= alpha)
	return result


def get_arc_from_points(p: List[Point]) -> Optional[Tuple[float, float, float, float, float]]:
	if len(p) == 3:
		a = p[0].x - p[1].x
		b = p[0].y - p[1].y
		c = p[2].x - p[1].x
		d = p[2].y - p[1].y
		e = a * (p[1].x + p[0].x) + b * (p[1].y + p[0].y)
		f = c * (p[1].x + p[2].x) + d * (p[1].y + p[2].y)
		g = 2 * (a * (p[2].y - p[0].y) - b * (p[2].x - p[0].x))
		# Points not on one line
		if g != 0:
			# Center point
			center_x = (d * e - b * f) / g + 0
			center_y = (a * f - c * e) / g + 0
			# radius
			radius = math.sqrt(math.pow(p[1].x - center_x, 2) + math.pow(p[1].y - center_y, 2))
			# Start angle
			start_angle = math.degrees(math.atan2(p[0].y - center_y, p[0].x - center_x))
			# End angle
			stop_angle = math.degrees(math.atan2(p[2].y - center_y, p[2].x - center_x))
			# If second point from opposite side
			if not is_angle_cross_arc(
				math.degrees(math.atan2(p[1].y - center_y, p[1].x - center_x)),
				start_angle,
				stop_angle
			):
				start_angle, stop_angle = stop_angle, start_angle

			return center_x, center_y, radius, start_angle, stop_angle

	return None
