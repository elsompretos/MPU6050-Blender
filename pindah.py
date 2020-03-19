import serial
import bge
import bpy
import mathutils
import math

qw = 0.0
qx = 0.0
qy = 0.0
qz = 0.0
 
ser = serial.Serial()
ser.baudrate = 115200
ser.port = "COM7"
ser.close()
ser.open()

# 0.95,-0.03,-0.00,-0.31
 
def Port():
    global qw, qx, qy, qz
    a = ser.readline().strip()
    a = a.decode("ascii").split(",")
    qw, qx, qy, qz = [float(s) for s in a]
    
def Cube():
    global qw, qx, qy, qz
    cont = bge.logic.getCurrentController()
    obj = cont.owner
    
    obj["qw"] = qw
    obj["qx"] = qx
    obj["qy"] = qy
    obj["qz"] = qz
    
    trunk = mathutils.Quaternion((obj["qw"], obj["qx"], obj["qy"], obj["qz"]))
    #correction = mathutils.Quaternion((0.0, 0.0, 1.0), math.radians(90.0))
    #trunk_out = correction*trunk
    obj.localOrientation = trunk

def execute_after_game( scene ):
    ser.close()
 
bpy.app.handlers.game_post.append( execute_after_game )


