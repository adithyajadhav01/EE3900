import lcapy as lc
from lcapy.discretetime import z

Y_z = (z**(2)+2*z)/(z**(2)-z-1)
y_n = Y_z.IZT()

print(y_n)