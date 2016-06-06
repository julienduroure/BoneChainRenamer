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
from .ops import *

class QuickRiggingPreferences(bpy.types.AddonPreferences):
	bl_idname = __package__

	bpy.types.Scene.quickrigging_prefs_current_suffix_index = bpy.props.IntProperty(default=-1)

	def draw(self, context):
		layout = self.layout

		if context.scene.quickrigging_prefs_datainited == True:
			row = layout.row()

			index = context.scene.quickrigging_prefs_current_suffix_index

			col = row.column()
			col.template_list("UI_UL_list", "quickrigging_prefs_suffix_list_list", context.scene, "quickrigging_prefs_suffix_list", context.scene, "quickrigging_prefs_current_suffix_index")
			col.label(text="Suffix List")
			col.prop(context.scene,"quickrigging_prefs_bone_separator", text="Separator")
			col.prop(context.scene,"quickrigging_prefs_count", text="Couting method")
			col = row.column(align=True)
			col.operator("wm.quickrigging_prefs_suffix_add", icon='ZOOMIN', text="")
			col.operator("wm.quickrigging_prefs_suffix_remove", icon='ZOOMOUT', text="").suffix_index = index


			col = row.column()
			col.prop(context.scene,"quickrigging_prefs_bonesegment", text="Segments for bones")

		else:
			layout.label("Warning, you have to init data before using this addon", icon="ERROR")
			layout.operator(InitAddonOperator.bl_idname, text=InitAddonOperator.bl_label)

def register():
	bpy.utils.register_class(QuickRiggingPreferences)

def unregister():
	bpy.utils.unregister_class(QuickRiggingPreferences)
