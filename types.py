import bpy
import mathutils

scene_objects = bpy.data.objects

print(list(scene_objects)) # or bpy.data.objects[:]

my_cube = bpy.data.objects["Cube"]
my_cube.delta_location += mathutils.Vector((1,1,1))

print(my_cube.delta_location)


#for type in bpy.types:
#    print(type)
# Module not iterable

#print(bpy.types['Cube'])
# Module object is non subscriptable?
