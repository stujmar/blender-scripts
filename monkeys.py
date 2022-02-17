import bpy
from random import randint
x, y, z = 0, 0, 0
monkeys = 100

bpy.ops.mesh.primitive_monkey_add(location=(x,y,z))
print(bpy)

while monkeys > 0:
    x =  randint(0, 25)
    y =  randint(0, 25)
    z =  randint(0, 25)
    bpy.ops.mesh.primitive_monkey_add(location=(x,y,z), rotation=(x,y,z))
    monkeys = monkeys - 1
    
