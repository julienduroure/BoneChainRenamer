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

from .glob import *
from .ui_panel import *

def get_suffix_length(suffix):
	len_ = []
	for suf in suffix:
		len_.append(len(suf))
	return list(set(len_))

def get_count(int_):
	if addonpref().ju_bcr_count == "INT":
		count = str(int_)
	elif addonpref().ju_bcr_count == "ALPHA":
		count = chr(int_ + ord('a'))
	else:
		count = str(int_) #default
	return count

def set_new_suffix_in_prefs(left,right):
	idx = len(addonpref().ju_bcr_suffix)
	suff = addonpref().ju_bcr_suffix.add()
	suff.left  = left
	suff.right = right
	addonpref().ju_bcr_suffix_index = idx

def set_default_values():
	set_new_suffix_in_prefs(".L", ".R")
	set_new_suffix_in_prefs(".l", ".r")
	set_new_suffix_in_prefs("left", "right")
	addonpref().ju_bcr_separator = "_"

#shortcut to prefs
def addonpref():
	user_preferences = bpy.context.user_preferences
	return user_preferences.addons[__package__].preferences

def update_panel(self, context):
	bpy.utils.unregister_class(JuBCR_Panel)

	JuBCR_Panel.bl_category = addonpref().category

	bpy.utils.register_class(JuBCR_Panel)
