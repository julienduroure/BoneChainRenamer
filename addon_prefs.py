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
from .utils import *

class JuBCR_SuffixItem(bpy.types.PropertyGroup):
	left  = bpy.props.StringProperty(default="")
	right = bpy.props.StringProperty(default="")

class JuBCR_AddonPref(bpy.types.AddonPreferences):
	bl_idname = __package__

	ju_bcr_suffix_index = bpy.props.IntProperty(default=-1)
	ju_bcr_suffix          = bpy.props.CollectionProperty(type=JuBCR_SuffixItem)
	ju_bcr_separator       = bpy.props.StringProperty(default="_")
	ju_bcr_count          		= bpy.props.EnumProperty(items=JuBCR_count_items, default="INT")

	category = bpy.props.StringProperty(name="Category", default="BoneChainRenamer", update=update_panel)

	def draw(self, context):
		layout = self.layout

		row_global = layout.row()

		index = self.ju_bcr_suffix_index

		box = row_global.box()
		row = box.row()
		col = row.column()
		row_ = col.row()
		row_.prop(self,"ju_bcr_separator", text="Separator")
		row_ = col.row()
		row_.prop(self,"ju_bcr_count", text="Counting method")
		col = row.column()
		row_ = col.row()
		if len(addonpref().ju_bcr_suffix) > 0:
			col_ = row_.column()
			col_.template_list("POSE_UL_JuBCR_SideList", "", addonpref(), "ju_bcr_suffix", addonpref(), "ju_bcr_suffix_index")

			col_ = row_.column(align=True)
			col_.operator("wm.ju_bcr_suffix_add", icon='ZOOMIN', text="")
			col_.operator("wm.ju_bcr_suffix_remove", icon='ZOOMOUT', text="").suffix_index = index
		else:
			row_.operator(InitAddonOperator.bl_idname, text=InitAddonOperator.bl_label)

		row_global = layout.row()
		box = row_global.box()
		row = box.row()
		row.prop(self, "category")


def register():
	bpy.utils.register_class(JuBCR_SuffixItem)
	bpy.utils.register_class(JuBCR_AddonPref)

def unregister():
	bpy.utils.unregister_class(JuBCR_SuffixItem)
	bpy.utils.unregister_class(JuBCR_AddonPref)
