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

bl_info = {
	"name": "Bone Chain Renamer",
	"author": "Julien Duroure",
	"version": (0, 0, 1),
	"blender": (2,77, 0),
	"description": "Bone Chain Renamer",
	"category": "Rigging",
}

if "bpy" in locals():
    import imp
    imp.reload(addon_prefs)
    imp.reload(glob)
    imp.reload(utils)
    imp.reload(ui_list)
    imp.reload(ui_ops)
    imp.reload(ui_panel)
    imp.reload(ops)
else:
    from .addon_prefs import *
    from .glob import *
    from .utils import *
    from .ui_list import *
    from .ui_ops import *
    from .ui_panel import *
    from .ops import *


import bpy

def register():
	ops.register()
	addon_prefs.register()
	glob.register()
	ui_ops.register()
	ui_panel.register()
	ui_list.register()

	bpy.types.Scene.quickrigging_prefs_bone_separator = bpy.props.StringProperty()
	bpy.types.Scene.quickrigging_prefs_count          = bpy.props.EnumProperty(items=quickrigging_prefs_count_items,
                                                    		default="INT",
                                                    		)

def unregister():
	addon_prefs.unregister()
	glob.unregister()
	ops.unregister()
	ui_ops.unregister()
	ui_panel.unregister()
	ui_list.unregister()

	del bpy.types.Scene.quickrigging_prefs_suffix_list
	del bpy.types.Scene.quickrigging_prefs_bone_separator
	del bpy.types.Scene.quickrigging_prefs_count
