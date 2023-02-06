import struct 
from dataclasses import dataclass
from enum import IntEnum
from threading import Thread
from queue import Queue

DRAG_END = 4294967295
class Code(IntEnum):
	ABS_X = 1
	ABS_Y = 0
	X = 54
	Y = 53
	UPDOWN = 57

@dataclass
class Frame:
	x: int
	y: int
	drag: int = -1

class ScreenInput:

	def __init__(self, queue):
		self.queue = queue
		self.thread = None

	def start(self):
		self.thread = Thread(target = self._readloop)
		self.thread.start()

	def _readloop(self):
		f = open( "/dev/input/event1", "rb" ); # Open the file in the read-binary mode
		cur = Frame(-1,-1,0)
		while True:
			frame = self._read_frame(f)
			if(frame.x == -1):
				frame.x = cur.x
			else:
				cur.x = frame.x
			if(frame.y == -1):
				frame.y = cur.y
			else:
				cur.y = frame.y
			queue.put(frame)

	def _read_frame(self, f):
		frame = Frame(-1,-1)
		while True:
			typ, code, val = self._read_one(f)
			if(typ == 0 and code == 0 and val == 0):
				return frame
			if(typ == 3):
				if code == Code.ABS_X:
						frame.x = val
				elif code == Code.ABS_Y:
						frame.y = val
				elif code == Code.UPDOWN:
						frame.drag = 0 if val == DRAG_END else 1

	def _read_one(self, f):
			data = f.read(24)
			ev = struct.unpack('4IHHI',data)
			typ = ev[4]
			code = ev[5]
			val = ev[6]
			return (typ,code,val)

if __name__ == "__main__":
	queue = Queue()
	screen = ScreenInput(queue)
	screen.start()
	while True:
		point = queue.get()
		print(point)
