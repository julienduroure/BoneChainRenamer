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

class QuickRiggingPanel(bpy.types.Panel):
    bl_label  = "Quick Rigging"
    bl_idname = "quick_rigging"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_category = "Quick Rigging"

    @classmethod
    def poll(self, context):
        return True #TODO armature + edit_mode

    def draw(self, context):
        if bpy.context.scene.quickrigging_prefs_datainited == False:
        	pass
		#TODO Warning message

        col = self.layout.column()
        col.operator("bones.chain_rename")

def register():
    bpy.utils.register_class(QuickRiggingPanel)

def unregister():
    bpy.utils.unregister_class(QuickRiggingPanel)    
