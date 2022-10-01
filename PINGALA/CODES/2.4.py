import lcapy as lc
from lcapy.discretetime import z

X_z = z**(2)/(z**(2)-z-1)
X_n = X_z.IZT()

print(X_n)