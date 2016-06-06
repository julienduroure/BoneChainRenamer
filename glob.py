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

quickrigging_prefs_count_items = [
    ("INT", "Integer", "Integer", 1),
    ("ALPHA", "Letter", "Alphanumeric", 2),
]

class SuffixItem(bpy.types.PropertyGroup):
	suffix = bpy.props.StringProperty(name="suffix", default="")

def register():
    bpy.utils.register_class(SuffixItem)

def unregister():
    bpy.utils.unregister_class(SuffixItem)
