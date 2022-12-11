import math

punto= (1.5, 3.6)
print(f"La coordinata x del punto è {punto[0]}")
t= [(1.5, 3.6), (-1.0, 0.0), (5.1, 4.3)]
print(f"la coordinata y del secondo vertice è {t[1][1]} ")
area=1/2*abs(t[0][0]*t[1][1]+t[0][1]*t[2][0]+t[1][0]*t[2][1]+t[2][0]*t[1][1]-t[2][1]*t[0][0]-t[1][0]*t[0][1])
print(area)


