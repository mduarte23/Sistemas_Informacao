import math

lat1= float(input('Digite a coordenada da latitude 1: '))
long1 = float(input('Digite a coordenada da longitude 1: '))
lat2= float(input('Digite a coordenada da latitude 2: '))
long2 = float(input('Digite a coordenada da latitude 2: '))
lat3= float(input('Digite a coordenada da latitude 3: '))
long3 = float(input('Digite a coordenada da longitude 3: '))

d1= math.sqrt((lat1-lat2)**2+(long2-long3)**2)
d2= math.sqrt((lat2-lat3)**2+(long2-long3)**2)
d3=math.sqrt((lat3-lat1)**2+(long3-long1)**2)

if (d1==d2) and (d2 == d3) and (d3 == d1):
    print('O triangulo é equilátero.')
elif (d1 == d2) or (d2 == d3) or (d3 == d1):
    print ('O triângulo é isóceles.')
else :
    print ('o triângulo é escaleno.')