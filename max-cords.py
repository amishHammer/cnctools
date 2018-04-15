from pygcode import Line
from pygcode import Machine, GCodeRapidMove
import re
import sys

m = Machine()
min_x = 0
max_x = 0
min_y = 0
max_y = 0
min_z = 0
max_z = 0


with open(sys.argv[1], 'r') as fh:
    for line_text in fh.readlines():
        ma = re.match(r'^M8.*$', line_text)
        if (ma):
            continue
        ma = re.match(r'^S.*$', line_text)
        if (ma):
            continue
        ma = re.search(r'\sG50\s', line_text)
        if (ma):
            line_text = re.sub(r'\sG50\s', '', line_text)
        line = Line(line_text)
        m.process_block(line.block)
        if (m.pos.X < min_x):
            min_x = m.pos.X
        if (m.pos.X > max_x):
            max_x = m.pos.X
        if (m.pos.Y < min_y):
            min_y = m.pos.Y
        if (m.pos.Y > max_y):
            max_y = m.pos.Y
        if (m.pos.Z < min_z):
            min_z = m.pos.Z
        if (m.pos.Z > max_z):
            max_z = m.pos.Z


print ("Min X: %f" % min_x)
print ("Max X: %f" % max_x)
print ("Min Y: %f" % min_y)
print ("Max Y: %f" % max_y)
print ("Min Z: %f" % min_z)
print ("Max Z: %f" % max_z)

if (min_x < 0):
    min_x *= -1
if (max_x < 0):
    max_x *= -1
if (min_y < 0):
    min_y *= -1
if (max_y < 0):
    max_y *= -1
if (min_z < 0):
    min_z *= -1
if (max_z < 0):
    max_z *= -1

print ("X Travel: %f" % (min_x + max_x));
print ("Y Travel: %f" % (min_y + max_y));
print ("Z Travel: %f" % (min_z + max_z));


