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
#	Copyright 2016 Julien Duroure (contact@julienduroure.com)
#
##########################################################################################

import bpy

from .utils import *
from .ui_panel import *

JuBCR_count_items = [
    ("INT", "Integer", "Integer", 1),
    ("ALPHA", "Letter", "Alphanumeric", 2),
]

JuCR_sort_type_items = [
    ("ALPHABETIC", "Alphabetic", "Alphabetic", 1),
	("X_LOC", "X Location", "X Location", 2),
	("Y_LOC", "Y Location", "Y Location", 3),
	("Z_LOC", "Z Location", "Z Location", 4),
	("X_LOC_REV", "-X Location", "-X Location", 5),
	("Y_LOC_REV", "-Y Location", "-Y Location", 6),
	("Z_LOC_REV", "-Z Location", "-Z Location", 7),
	("DISTANCE", "Distance", "Distance", 8),
	("DISTANCE_REV", "Distance Reversed", "Distance Reversed", 9),	
]

def register():
    pass

def unregister():
    pass
