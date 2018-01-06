#
# BoneChainRenamer is part of BleRiFa. http://BleRiFa.com
#
##########################################################################################
#	GPL LICENSE:
#-------------------------
# This file is part of BoneChainRenamer.
#
#    BoneChainRenamer is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    BoneChainRenamer is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with BoneChainRenamer.  If not, see <http://www.gnu.org/licenses/>.
##########################################################################################
#
#	Copyright 2016-2018 Julien Duroure (contact@julienduroure.com)
#
##########################################################################################

import bpy

from .glob import *
from .utils import *
import operator

def sort_location(obj, tab_bones, item, reversed):
	locations = []
	for bone in tab_bones:
		loc = obj.location + bpy.context.active_object.data.bones[bone].head_local
		locations.append((bone, loc[item]))
	if reversed == False:
		return [bone[0] for bone in sorted(locations, key=operator.itemgetter(1))]
	else:
		return [bone[0] for bone in sorted(locations, key=operator.itemgetter(1))][::-1]

def sort_distance(obj, ref_bone, tab_bones, reversed):
	distances = []
	for bone in tab_bones:
		dist = ((obj.data.bones[ref_bone.name].head_local - obj.data.bones[ref_bone.name].tail_local)/2 - (bpy.context.active_object.data.bones[bone].head_local - bpy.context.active_object.data.bones[bone].tail_local)/2).length
		distances.append((bone, dist))
	if reversed == False:
		return [bone[0] for bone in sorted(distances, key=operator.itemgetter(1))]
	else:
		return [bone[0] for bone in sorted(distances, key=operator.itemgetter(1))][::-1]
