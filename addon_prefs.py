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

class JuBCR_SuffixItem(bpy.types.PropertyGroup):
	left  = bpy.props.StringProperty(default="")
	right = bpy.props.StringProperty(default="")

class JuBCR_AddonPref(bpy.types.AddonPreferences):
	bl_idname = __package__

	ju_bcr_suffix_index = bpy.props.IntProperty(default=-1)
	ju_bcr_suffix          = bpy.props.CollectionProperty(type=JuBCR_SuffixItem)
	ju_bcr_separator       = bpy.props.StringProperty()
	ju_bcr_count          		= bpy.props.EnumProperty(items=JuBCR_count_items, default="INT")

	def draw(self, context):
		layout = self.layout

		if len(addonpref().ju_bcr_suffix) > 0:
			row = layout.row()

			index = self.ju_bcr_suffix_index

			col = row.column()
			col.template_list("POSE_UL_JuBCR_SideList", "", addonpref(), "ju_bcr_suffix", addonpref(), "ju_bcr_suffix_index")
			col.prop(self,"ju_bcr_separator", text="Separator")
			col.prop(self,"ju_bcr_count", text="Couting method")
			col = row.column(align=True)
			col.operator("wm.ju_bcr_suffix_add", icon='ZOOMIN', text="")
			col.operator("wm.ju_bcr_suffix_remove", icon='ZOOMOUT', text="").suffix_index = index

		else:
			layout.label("Warning, you have to init data before using this addon", icon="ERROR")
			layout.operator(InitAddonOperator.bl_idname, text=InitAddonOperator.bl_label)

def register():
	bpy.utils.register_class(JuBCR_SuffixItem)
	bpy.utils.register_class(JuBCR_AddonPref)

def unregister():
	bpy.utils.unregister_class(JuBCR_SuffixItem)
	bpy.utils.unregister_class(JuBCR_AddonPref)
