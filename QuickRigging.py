bl_info = {
	"name": "Quick Rigging",
	"author": "Julien Duroure",
	"version": (0, 0, 1),
	"blender": (2,72, 0),
	"description": "Tools for Rigging",
	"category": "Rigging",	 
}


#TODO
# Panel to be created

#Set scale from active : 
# * strange selection at the end
# * if there is already a copy scale modifier, and launch tool --> 2 second one is added. Needed ?


quickrigging_prefs_count_items = [
    ("INT", "Integer", "Integer", 1),
    ("ALPHA", "Letter", "Alphanumeric", 2),
]


import bpy

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

class SuffixItem(bpy.types.PropertyGroup):
	suffix = bpy.props.StringProperty(name="suffix", default="")


class QuickRiggingPreferences(bpy.types.AddonPreferences):
	bl_idname = __name__

	bpy.types.Scene.quickrigging_prefs_current_suffix_index = bpy.props.IntProperty(default=-1)

	def draw(self, context):
		layout = self.layout

		if context.scene.quickrigging_prefs_datainited == True:
			layout.prop(context.scene, "quickrigging_prefs_tab1", text="Preferences", icon="QUESTION")
			if context.scene.quickrigging_prefs_tab1:
				layout.label(text="Here are Quick Rigging Addon Preferences.")
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

			layout.prop(context.scene, "quickrigging_prefs_tab2", text="Infos", icon="URL")
			if context.scene.quickrigging_prefs_tab2:
				row = layout.row()
				row.operator("wm.url_open", text="julienduroure.com").url = "http://julienduroure.com/"
				row.operator("wm.url_open", text="Julien Duroure's Ghitub").url = "https://github.com/julienduroure/scripts"
		else:
			layout.label("Warning, you have to init data before using this addon", icon="ERROR")
			layout.operator(InitAddonOperator.bl_idname, text=InitAddonOperator.bl_label)
			

class InitAddonOperator(bpy.types.Operator):
	bl_idname = "scene.init_addon"
	bl_label = "Init Quick Rigging Addon"
 
	@classmethod
	def poll(cls, context):
		return True
 
	def execute(self, context):
		set_default_values()
		bpy.context.scene.quickrigging_prefs_datainited = True

		return {'FINISHED'}
	
def get_suffix_length(suffix):
	len_ = []
	for suf in suffix:
		len_.append(len(suf))
	return list(set(len_))

def get_count(int_):
	if bpy.context.scene.quickrigging_prefs_count == "INT":
		count = str(int_)
	elif bpy.context.scene.quickrigging_prefs_count == "ALPHA":
		count = chr(int_ + ord('a'))
	else:
		count = str(int_) #default
	return count

class BoneChainRename(bpy.types.Operator):
	bl_idname = 'bones.chain_rename'
	bl_label  = "Bone Chain Rename"
	bl_options = {'REGISTER', 'UNDO'}
	
	def execute(self, context):

		# check addon is initialized
		if context.scene.quickrigging_prefs_datainited == False:
			self.report(type={"ERROR"},message="Addon is not initialized")
			return {'CANCELLED'}
		
		side_suffix_ = context.scene.quickrigging_prefs_suffix_list
		side_suffix  = []
		for suf in side_suffix_:
			side_suffix.append(suf.name)
		len_ = get_suffix_length(side_suffix)

		separator = context.scene.quickrigging_prefs_bone_separator

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

		while True:
			tmp_name = active_bone_name_root + count + suffix
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
					updates.append([child.name, new_name])
					current_bone = child.name
				else:
					child_bone = False
			
		for bone in updates:
			bones[bone[0]].name = bone[1]

		
		return {'FINISHED'}
		
		

def set_new_suffix_in_prefs(suf):
	idx = len(bpy.context.scene.quickrigging_prefs_suffix_list)
	suff = bpy.context.scene.quickrigging_prefs_suffix_list.add()
	suff.name = suf
	bpy.context.scene.quickrigging_prefs_current_suffix_index = idx

def set_default_values():
	set_new_suffix_in_prefs(".L")
	set_new_suffix_in_prefs(".R")
	set_new_suffix_in_prefs(".l")
	set_new_suffix_in_prefs(".r")
	set_new_suffix_in_prefs("left")
	set_new_suffix_in_prefs("right")
	bpy.context.scene.quickrigging_prefs_bone_separator = "_"
	
	
		
# keymap

addon_keymaps = []
	   
def register():

	bpy.types.Scene.quickrigging_prefs_tab1 = bpy.props.BoolProperty(default=False)
	bpy.types.Scene.quickrigging_prefs_tab2 = bpy.props.BoolProperty(default=False)

	# Panel
	bpy.utils.register_class(QuickRiggingPanel)
	
	# Operators
	bpy.utils.register_class(InitAddonOperator)
	bpy.utils.register_class(BoneChainRename)


	# Preferences
	bpy.utils.register_class(SuffixItem)
	bpy.utils.register_class(WM_OT_quickrigging_prefs_suffix_add)
	bpy.utils.register_class(WM_OT_quickrigging_prefs_suffix_remove)
	bpy.types.Scene.quickrigging_prefs_suffix_list    = bpy.props.CollectionProperty(type=SuffixItem)
	bpy.types.Scene.quickrigging_prefs_bone_separator = bpy.props.StringProperty()
	bpy.types.Scene.quickrigging_prefs_count          = bpy.props.EnumProperty(items=quickrigging_prefs_count_items,
                                                    		default="INT",
                                                    		)
	bpy.types.Scene.quickrigging_prefs_datainited     = bpy.props.BoolProperty(default=False)
	bpy.utils.register_class(QuickRiggingPreferences)




	
def unregister():


	# Panel
	bpy.utils.unregister_class(QuickRiggingPanel)
	
	# Operators
	bpy.utils.unregister_class(InitAddonOperator)
	bpy.utils.unregister_class(BoneChainRename)

	# Preferences
	bpy.utils.unregister_class(SuffixItem)
	bpy.utils.unregister_class(WM_OT_quickrigging_prefs_suffix_add)
	bpy.utils.unregister_class(WM_OT_quickrigging_prefs_suffix_remove)
	bpy.utils.unregister_class(QuickRiggingPreferences)
	
if __name__ == "__main__":
	register()
