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

class InitAddonOperator(bpy.types.Operator):
	bl_idname = "pose.init_side_addon"
	bl_label = "Init Sides"

	@classmethod
	def poll(cls, context):
		return True

	def execute(self, context):
		set_default_values()

		return {'FINISHED'}

class BoneChainRename(bpy.types.Operator):
	bl_idname = 'bones.chain_rename'
	bl_label  = "Bone Chain Rename"
	bl_options = {'REGISTER', 'UNDO'}

	@classmethod
	def poll(cls, context):
		return context.active_object and context.active_object.type == "ARMATURE" and context.mode == 'EDIT_ARMATURE' and len(context.selected_bones) > 0

	def execute(self, context):

		# check addon is initialized
		if len(addonpref().ju_bcr_suffix) == 0:
			set_default_values()

		side_suffix_ = addonpref().ju_bcr_suffix
		side_suffix  = []
		for suf in side_suffix_:
			side_suffix.append(suf.left)
			side_suffix.append(suf.right)
		len_ = get_suffix_length(side_suffix)

		separator = addonpref().ju_bcr_separator

		selected_bone_names = []
		new_name_selected = {}
		#active_bone
		bones = []
		tree_bones = {}
		updates = []

		#update bones list
		bpy.ops.object.editmode_toggle()
		bpy.ops.object.editmode_toggle()

		#retrieve bones & active bone
		obj = bpy.context.active_object
		bones = bpy.data.armatures[obj.data.name].bones
		active_bone_name = bpy.context.active_bone.name

		#retrieve selected bones
		for bone in bpy.context.selected_bones:
			selected_bone_names.append(bone.name)

		#retrieve name without suffix (if needed)
		found = False
		for suf_len in len_:
			if active_bone_name[len(active_bone_name)-suf_len:len(active_bone_name)] in side_suffix:
				active_bone_name_root = active_bone_name[:len(active_bone_name)-suf_len]
				suffix = active_bone_name[len(active_bone_name)-suf_len:len(active_bone_name)]
				found = True
		if found == False: # without side suffix
			active_bone_name_root = active_bone_name
			suffix = ""

		selected_bone_names.sort()

		#retrieve next available cpt
		cpt = 0
		count = get_count(cpt)

		if len(selected_bone_names) == 1 and selected_bone_names[0] == active_bone_name and addonpref().ju_brc_single_chain_no_count == True:
			separator = ""
			count = ""
		else:
			while True:
				tmp_name = active_bone_name_root + separator + count + suffix
				found = False
				for bone in bones:
					if bone.name == tmp_name:
						found = True
						break
				if found == False:
					break
				else:
					cpt = cpt + 1
					count = get_count(cpt)

		#rename active bone
		updates.append([bones[active_bone_name].name,active_bone_name_root + separator + count + suffix])
		new_name_selected[bones[active_bone_name].name] = active_bone_name_root + separator + count + suffix

		#rename selected bones
		for bone in selected_bone_names:
			if bone != active_bone_name:
				#retrieve next available cpt
				cpt = 0
				count = get_count(cpt)
				while True:
					#check in selected bones
					tmp_name = active_bone_name_root + separator + count + suffix
					found = False
					for b_name in new_name_selected.values():
						if b_name == tmp_name:
							found = True
							break
					if found == False:
						# if not found in selected, check in already existing bones
						for b in bones:
							if b.name == tmp_name:
								found = True
								break
						if found == False:
							break
						else:
							cpt = cpt + 1
							count = get_count(cpt)
					else:
						cpt = cpt + 1
						count = get_count(cpt)

				updates.append([bones[bone].name, active_bone_name_root + separator + count + suffix])
				new_name_selected[bones[bone].name] = active_bone_name_root + separator + count + suffix


		# update children
		for bone in selected_bone_names:
			current_bone = bone
			child_bone   = True
			new_name	 = new_name_selected[bone]
			while child_bone:
				#loop on children
				if len(bones[current_bone].children) != 0:
					child = bones[current_bone].children[0]
					if child.use_connect == False and addonpref().ju_brc_stop_chain_not_connected == True:
						child_bone = False
					else:
						updates.append([child.name, new_name])
						current_bone = child.name
				else:
					child_bone = False

		for bone in updates:
			bones[bone[0]].name = bone[1]


		return {'FINISHED'}

def register():
	bpy.utils.register_class(InitAddonOperator)
	bpy.utils.register_class(BoneChainRename)

def unregister():
	bpy.utils.unregister_class(InitAddonOperator)
	bpy.utils.unregister_class(BoneChainRename)
