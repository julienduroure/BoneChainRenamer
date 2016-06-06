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
from .utils import *

class WM_OT_quickrigging_prefs_suffix_add(bpy.types.Operator):
	bl_idname = "wm.quickrigging_prefs_suffix_add"
	bl_label  = "Add Suffix"

	suffix_index = bpy.props.IntProperty()

	@classmethod
	def poll(cls, context):
		return bool(context.scene)

	def execute(self, context):
		scene = context.scene
		idx = len(scene.quickrigging_prefs_suffix_list)
		suff = scene.quickrigging_prefs_suffix_list.add()
		suff.name = "Enter new suffix here"
		scene.quickrigging_prefs_current_suffix_index = idx

		return {'FINISHED'}

class WM_OT_quickrigging_prefs_suffix_remove(bpy.types.Operator):
	bl_idname = "wm.quickrigging_prefs_suffix_remove"
	bl_label  = "Remove Suffix"

	suffix_index = bpy.props.IntProperty()

	@classmethod
	def poll(cls, context):
		return bool(context.scene)

	def execute(self, context):
		scene = context.scene
		idx = self.suffix_index
		scene.quickrigging_prefs_suffix_list.remove(idx)
		if scene.quickrigging_prefs_current_suffix_index > len(scene.quickrigging_prefs_suffix_list) - 1:
			scene.quickrigging_prefs_current_suffix_index = len(scene.quickrigging_prefs_suffix_list) - 1

		return {'FINISHED'}

def register():
	bpy.utils.register_class(WM_OT_quickrigging_prefs_suffix_add)
	bpy.utils.register_class(WM_OT_quickrigging_prefs_suffix_remove)

def unregister():
	bpy.utils.unregister_class(WM_OT_quickrigging_prefs_suffix_add)
	bpy.utils.unregister_class(WM_OT_quickrigging_prefs_suffix_remove)	
