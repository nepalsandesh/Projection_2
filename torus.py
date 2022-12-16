import math

R = 1
r = 0.5

points = []
indexes = []

for u in range(0, 360, 10):
    for v in range(0, 360, 10):
        x = (R + r * math.cos(math.radians(v))) * math.cos(math.radians(u))
        y = (R + r * math.cos(math.radians(v))) * math.sin(math.radians(u))
        z = r * math.sin(math.radians(v))
        points.append((x, y, z))

for i in range(0, len(points)-36):
    if (i+1) % 36 != 0:
        indexes.append((i, i+1, i+36))
        indexes.append((i+1, i+36, i+37))
    else:
        indexes.append((i, i-35, i+36))
        indexes.append((i-35, i+36, i+1))

def Points():
    return points

def Indexes():
    return indexes