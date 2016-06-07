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

def get_suffix_length(suffix):
	len_ = []
	for suf in suffix:
		len_.append(len(suf))
	return list(set(len_))

def get_count(int_):
	if addonpref().quickrigging_prefs_count == "INT":
		count = str(int_)
	elif addonpref().quickrigging_prefs_count == "ALPHA":
		count = chr(int_ + ord('a'))
	else:
		count = str(int_) #default
	return count

def set_new_suffix_in_prefs(left,right):
	idx = len(addonpref().quickrigging_prefs_suffix_list)
	suff = addonpref().quickrigging_prefs_suffix_list.add()
	suff.left  = left
	suff.right = right
	addonpref().quickrigging_prefs_current_suffix_index = idx

def set_default_values():
	set_new_suffix_in_prefs(".L", ".R")
	set_new_suffix_in_prefs(".l", ".r")
	set_new_suffix_in_prefs("left", "right")
	addonpref().quickrigging_prefs_bone_separator = "_"

#shortcut to prefs
def addonpref():
	user_preferences = bpy.context.user_preferences
	return user_preferences.addons[__package__].preferences
