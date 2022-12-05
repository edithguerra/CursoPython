#TUPLAS
amigos=[] ##lista vacia
amigos2=[1,2,3]
amigos3=['a','b']
amigos4=[False,True]
amigos5=['hola',False]
print(amigos5)
amigos5[1]='chao'
print(amigos5)
len(amigos)


casaDiego=[
    [1,2,3,]
    [1,'diego',3,4]
]
casaDiego[1][1]='julissa'
casaDiego[1][3]='diego'
print(casaDiego)

casaEdith=[
[1,2,3,4,5],
[1,2,3,4,5],
[1,2,3,4,5],
[1,2,3,4,5],
[1,2,3,4,5]
]

i0=[0,1,1,1,1]
i1=[1,0,1,1,1]
i2=[1,1,0,1,1]
i3=[1,1,1,0,1]
i4=[1,1,1,1,0]

for i in range(0,len(casaEdith)):
    for j in range(0,len(casaEdith)):
        casaEdith[i][j]=1
        casaEdith[i][i]=0
print(casaEdith)

i0=[0,1,1,1,0]
i1=[1,0,1,0,1]
i2=[1,1,0,1,1]
i3=[1,0,1,0,1]
i4=[0,1,1,1,0]

contador=4
for i in range(0,len(casaEdith)):
    for j in range(0,len(casaEdith[i])):
        casaEdith[i][j] = 1
        casaEdith[i][i] = 0
        casaEdith[i][contador]=0
    if contador>=0:
        contador=contador-1
        print(casaEdith[i], end="\n")
        print(contador)