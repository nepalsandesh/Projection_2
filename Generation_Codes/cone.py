import math

# Number of points around the circumference of the base
n = 100

# Radius and height of the cone
r = 4
h = 10

# Generate the coordinates for the points on the surface of the cone
coords = []
for i in range(n):
    theta = 2 * math.pi * i / n
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    z = h
    coords.append((x, y, z))

# Generate the coordinates for the base of the cone
for i in range(n):
    theta = 2 * math.pi * i / n
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    z = 0
    coords.append((x, y, z))

# Round the floating point numbers to 3 decimal places
coords = [(round(x, 3), round(y, 3), round(z, 3)) for x, y, z in coords]

# Print the coordinates
print(coords)
