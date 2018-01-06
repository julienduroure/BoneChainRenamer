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

bl_info = {
	"name": "Bone Chain Renamer",
	"author": "Julien Duroure",
	"version": (0, 1, 0),
	"blender": (2,79, 0),
	"description": "Bone Chain Renamer",
	"category": "Rigging",
	"location": "View 3D tools, tab 'BoneChainRenamer'",
	"wiki_url": "http://blerifa.com/BoneChainRenamer/",
	"tracker_url": "https://github.com/julienduroure/BleRiFa/issues/",
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
    imp.reload(sort_type)
else:
    from .addon_prefs import *
    from .glob import *
    from .utils import *
    from .ui_list import *
    from .ui_ops import *
    from .ui_panel import *
    from .ops import *
    from .sort_type import *


import bpy

def register():
	ops.register()
	addon_prefs.register()
	glob.register()
	ui_ops.register()
	ui_panel.register()
	ui_list.register()

def unregister():
	addon_prefs.unregister()
	glob.unregister()
	ops.unregister()
	ui_ops.unregister()
	ui_panel.unregister()
	ui_list.unregister()
