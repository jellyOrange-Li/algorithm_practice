from math import sin
from math import pi

x = []
for i in range(1,128):
    x.append(int(sin(2 * pi * i / 128) * 2048) + 2048)
print(x)


