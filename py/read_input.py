import struct 
from enum import IntEnum

# sample app to read input events from touchscreen i2c
# some help from https://thehackerdiary.wordpress.com/tag/devinput-python/

f = open( "/dev/input/event1", "rb" ); # Open the file in the read-binary mode

DRAG_END = 4294967295
class Code(IntEnum):
    X = 54
    Y = 53
    UPDOWN = 57


x_pos = -1;
y_pos = -1;
dragging = False

while 1:
  data = f.read(24)
  ev = struct.unpack('4IHHI',data)
  code = ev[5]
  val = ev[6]
  #print(ev)
  #print(f"{code} {val}")
  if(code == Code.X or Code.Y):
      if(code == Code.X):
          x_pos = val
      if(code == Code.Y):
          y_pos = val
      print(f"{x_pos},{y_pos}")
  if(code == Code.UPDOWN):
      if(val == DRAG_END):
        print("drag stopped")
        dragging = False
      else:
        print("drag started")
        dragging = True
