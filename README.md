# LIPRO
> This is the documentation of LIPRO which is written in Python. Examples provided here are self-contained and presented for better understanding of users.

### Required libraries

[OpenCV-python](https://pypi.org/project/opencv-python "LCO")\
[Numpy](https://numpy.org/doc "LCO")\
[Shapely](https://shapely.readthedocs.io/en/stable/manual.html "LCO")\
[Numpy-stl](https://pypi.org/project/numpy-stl/ "LCO")\
[Scipy](https://www.scipy.org/docs.html "LCO")

Since LIPRO is written in Python, it uses the basic data structure list to present vectors and directions. 
```sh
v1 = [0,0,1]

curve = [[0,0,0],[10,5,5],[10,10,10]]
```
In order to have 2D polygons, function polygon(radius,Num of edges, starting angle) is presented.

```sh
poly1 = polygon(10,4,0)
```
Having a guide curve and two closed 2D polygons (start and end of the guide curve), we can generate a 3D model and present it as STL or OBJ files.

```sh
vertices, faces = sweep(poly1, poly2, guide curve, twist angle=0, scale=None)
savestl('name of the part', vertices, faces)
```

There is also a transformation function to move and rotate each part in space based on cartesian coordinates. 
```sh
part = Transform(object,thx=0,thy=0,thz=0,dx=0,dy=0,dz=0)
```
where thx,thy,thz are rotation around x,y,z axes and dx,dy,dz are translation along x,y,z axes. 


## Usage example

### Cube
To generate a cube, we only need to move a single square profile along a path as presented below. 

```python
from LIPRO import *

G1 = polygon(10,4)
S1 = [[0,0,0],[0,0,10*np.sqrt(2)]]
part1 = sweep(G1,G1,S1)

#savestl('cube',part1[0],part1[1])
```

<img src="https://user-images.githubusercontent.com/53440292/96132563-3ac15780-0f03-11eb-84f6-8301e2362cc3.png" width="30%">

### Bishop

Some profiles are too complicated to be designed by combination of polygons. Therefore, they can be loaded and used with sweep function.

```python
from LIPRO import *

profile1 = Load('text files/Bishop','profile')
path = polygon(4,50,90)
path = Transform(np.insert(path,2,0,axis=1),0,90,0,-4,0,0)
part1 = sweep(profile1,profile1,path)

#savestl('Bishop', part1[0],part1[1])
```

<img src="https://user-images.githubusercontent.com/53440292/96174975-d6b68780-0f32-11eb-953e-905a7f5765ed.JPG" width="40%">

### Donuts

Two parts can be designed separately and can join together to form a single part.

```python
from LIPRO import *

G1 = np.insert(polygon(1,50),2,0,axis=1)
G1 = Transform(G1,90,0,0,0,0,0)
S1 = np.array(polygon(1,50)) + [-1,0]
part1 = sweep(S1,S1,G1)
part1_ver = Transform(part1[0],0,0,0,0,0,1)

G2 = np.insert(polygon(1,50),2,0,axis=1)
G2 = Transform(G2,0,90,90,0,0,0)
S2 = np.array(polygon(1,50,90)) + [0,1]
part2 = sweep(S2,S2,G2)
part2_ver = Transform(part2[0],0,0,0,0,0,3)

#savestl('ring',part1_ver,part1[1])
#savestl('ring2',part2_ver,part2[1])
```

<img src="https://user-images.githubusercontent.com/53440292/96175871-2cd7fa80-0f34-11eb-917d-5444f4c313c8.jpg" width="50%">

### A path with multiple profiles

If along the guide curve there must be located more than two profiles, we can decompose the part into multiple subparts and use the sweep function to make each subpart. Afterwards, these subparts can be joined together to form the original part.
The number of subparts can be obtained from,

```sh
N = Number of profiles - 1
```
For instance in the following example there are three profiles as, 

<img src="https://user-images.githubusercontent.com/53440292/96190762-6a944d80-0f4b-11eb-8b64-0fee003f50e2.png" width="50%">

```python
from LIPRO import *

G1 = polygon(6,30)
G2 = polygon(3,3)
P1 = Transform(Load('t1')[:,[2,1,0]],-90,0,0,0,0,0)
part1 = sweep(G1,G2,P1)

G3 = polygon(3,10)
part2 = sweep(G2,G3,P1[:-3])
part22 = Transform(part2[0],0,0,0,0,P1[-1][1],P1[-1][2])

#savestl('h1',part1[0],part1[1])
#savestl('h2',part22,part2[1])
```

<img src="https://user-images.githubusercontent.com/53440292/96191009-e55d6880-0f4b-11eb-9382-36724de258c0.JPG" width="40%">
<img src="https://user-images.githubusercontent.com/53440292/96191042-fa39fc00-0f4b-11eb-92bc-d0cf5abc46f6.JPG" width="40%">
