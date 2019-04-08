#
# BoneChainRenamer is part of BleRiFa. http://BleRiFa.com
#
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
#	Copyright 2016-2018 Julien Duroure (contact@julienduroure.com)
#
##########################################################################################

import bpy

from .glob import *

class JuBCR_Panel(bpy.types.Panel):
    bl_label  = "Renamer"
    bl_idname = "bone_renamer"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "BoneChainRenamer"

    @classmethod
    def poll(self, context):
        return context.active_object and context.active_object.type == "ARMATURE" and context.mode == 'EDIT_ARMATURE'

    def draw(self, context):

        self.layout.operator("bones.chain_rename")

def register():
    bpy.utils.register_class(JuBCR_Panel)

def unregister():
    bpy.utils.unregister_class(JuBCR_Panel)
