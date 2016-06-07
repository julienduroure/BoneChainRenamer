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

class SuffixItem(bpy.types.PropertyGroup):
	left  = bpy.props.StringProperty(default="")
	right = bpy.props.StringProperty(default="")

class QuickRiggingPreferences(bpy.types.AddonPreferences):
	bl_idname = __package__

	quickrigging_prefs_current_suffix_index = bpy.props.IntProperty(default=-1)
	quickrigging_prefs_suffix_list          = bpy.props.CollectionProperty(type=SuffixItem)
	quickrigging_prefs_bone_separator       = bpy.props.StringProperty()
	quickrigging_prefs_count          		= bpy.props.EnumProperty(items=quickrigging_prefs_count_items, default="INT")

	def draw(self, context):
		layout = self.layout

		if len(addonpref().quickrigging_prefs_suffix_list) > 0:
			row = layout.row()

			index = self.quickrigging_prefs_current_suffix_index

			col = row.column()
			col.template_list("POSE_UL_JuBCR_SideList", "", addonpref(), "quickrigging_prefs_suffix_list", addonpref(), "quickrigging_prefs_current_suffix_index")
			col.prop(self,"quickrigging_prefs_bone_separator", text="Separator")
			col.prop(self,"quickrigging_prefs_count", text="Couting method")
			col = row.column(align=True)
			col.operator("wm.quickrigging_prefs_suffix_add", icon='ZOOMIN', text="")
			col.operator("wm.quickrigging_prefs_suffix_remove", icon='ZOOMOUT', text="").suffix_index = index

		else:
			layout.label("Warning, you have to init data before using this addon", icon="ERROR")
			layout.operator(InitAddonOperator.bl_idname, text=InitAddonOperator.bl_label)

def register():
	bpy.utils.register_class(SuffixItem)
	bpy.utils.register_class(QuickRiggingPreferences)

def unregister():
	bpy.utils.unregister_class(SuffixItem)
	bpy.utils.unregister_class(QuickRiggingPreferences)
