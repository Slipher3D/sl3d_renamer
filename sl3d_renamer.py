bl_info = {
    "blender": (2, 80, 0),
    "name":"Renamer",
    "category":"Object",
}

import bpy
import time

class RN_OT_Renamer(bpy.types.Operator):
    """"Object Rename Appender"""
    bl_idname = 'object.renamer'
    bl_label = 'Rename Selection'
    bl_options = {'REGISTER', 'UNDO'}

    name = bpy.props.StringProperty(name="Name", default="")
    prefix = bpy.props.StringProperty(name="Prefix", default="")
    suffix = bpy.props.StringProperty(name="Suffix", default="")

    def execute(self, context):
        time_start = time.time()
        sObjs = bpy.context.selected_objects

        if not self.name:

            for o in sObjs:
                on = o.name
                o.name = on + self.suffix
                on = o.name
                o.name = self.prefix + on

        else:
            for o in sObjs:
                o.name = self.name
                on = o.name
                o.name = on + self.suffix
                on = o.name
                o.name = self.prefix + on

        print("Script completed in: %.4f sec" % (time.time() - time_start))
        return {'FINISHED'}

def menu_func(self, context):
    self.layout.operator(ObjectCursorArray.bl_idname)

def register():
    bpy.utils.register_class(RN_OT_Renamer)
    bpy.types.VIEW3D_MT_object.append(menu_func)

def unregister():
    bpy.utils.unregister_class(RN_OT_Renamer)
    bpy.types.VIEW3D_MT_object.remove(menu_func)

if __name__ == "__main__":
    register()