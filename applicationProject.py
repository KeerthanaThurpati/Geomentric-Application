import streamlit as st
import time


def triangle_perimeter(a,b,c):
    return a+b+c
def triangle_area(a,b,c):
    s=(a+b+c)/2
    area=(s*(s-a)*(s-b)*(s-c))**0.5
    return area

def square_perimeter(s):
    return 4*s
def square_area(s):
    return s**2

def rectangle_perimeter(l,w):
    return 2*(l+w)
def rectangle_area(l,w):
    return l*w

def circle_perimeter(r):
    return 2*3.14*r

def circle_area(r):
    return 3.14*r**2




#3D objects

st.title('3D objects')

def TSA_cone(r,l):
    return 3.14*r*l+3.14*r**2

def volume_cone(r,l):
    return 1/3*3.14*(r**2)*((l**2)-(r**2))**(0.5)


def TSA_Cylinder(r,h):
    return 2*3.14*r*h+2*3.14*r**2

def volume_cylinder(r,h):
    return 3.14*r**2*h

def cube_tsa(s):
    return 6*s**2

def volume_cube(s):
    return s**3

def tsa_cuboid(l,w,h):
    return 2*(l*w+l*h+w*h)

def volume_cuboid(l,w,h):
    return l*w*h    

def tsa_sphere(r):
    return 4*3.14*r**2

def volume_sphere(r):
    return 4/3*3.14*r**3

st.title('Geometry Calculator')

st.header('2D Objects')

st.subheader('Triangle')

col1,col2=st.columns([1,3])

with col1:
    a=st.number_input('side a',0.0)
    b=st.number_input('side b',0.0)
    c=st.number_input('side c',0.0)

cola,colb=st.columns(2)

with cola:
    st.metric('Perimeter',triangle_perimeter(a,b,c))

with colb:
    st.metric('Area',triangle_area(a,b,c))

#############################################

st.divider()

st.subheader('Square')

col1s,col2s=st.columns([1,3])

with col1s:
    s=st.number_input('side s',0.0)

colas,colbs=st.columns(2)

with colas:
    st.metric('Perimeter',square_perimeter(s))

with colbs:
    st.metric('Area',square_area(s))

st.divider()

st.subheader('Rectangle')

col1r,col2r=st.columns([1,3])

with col1r:
    l=st.number_input('length l',0.0)
    w=st.number_input('width w',0.0)

colar,colbr=st.columns(2)
with colar:
    st.metric('Perimeter',rectangle_perimeter(l,w))

with colbr:
    st.metric('Area',rectangle_area(l,w))

st.divider()

st.subheader('Circle')

col1c,col2c=st.columns([1,3])

r=st.number_input('radius r',0.0)

colac,colbc=st.columns(2)

with colac:
    st.metric('Perimeter',circle_perimeter(r))


with colbc:
    st.metric('Area',circle_area(r))

st.divider()

st.header('3D Objects')

st.subheader('Cone')

col3,col4=st.columns([1,3])

with col3:
    cone_r=st.number_input('radius r',0.0,key='cone_r')
    cone_l=st.number_input('slant height l',0.0,key='cone_l')

col3dac,col3dbc=st.columns(2)

with col3dac:
    st.metric('TSA',TSA_cone(cone_r,cone_l))

with col3dbc:
    st.metric('Volume',volume_cone(cone_r,cone_l))


st.divider()

st.subheader('Cylinder')

col3cy,col4cy=st.columns([1,3])

with col3cy:
    cyl_r=st.number_input('radius r',0.0,key='cyl_r')
    cyl_h=st.number_input('height h',0.0,key='cyl_h')

col3dacy,col3dbcy=st.columns(2)

with col3dacy:
    st.metric('TSA',TSA_Cylinder(cyl_r,cyl_h))

with col3dbcy:
    st.metric('Volume',volume_cylinder(cyl_r,cyl_h))


st.divider()

st.subheader('Cube')

col3cu,col4cu=st.columns([1,3])

with col3cu:
    cube_side=st.number_input('side s',0.0,key='cube_side')

col3dacu,col3dbcu=st.columns(2)

with col3dacu:
    st.metric('TSA',cube_tsa(cube_side))

with col3dbcu:
    st.metric('Volume',volume_cube(cube_side))

st.divider()

st.subheader('Cuboid')

col3cb,col4cb=st.columns([1,3])

with col3cb:
    cuboid_l=st.number_input('Length l',0.0,key='cuboid_l')
    cuboid_w=st.number_input('Width w',0.0,key='cuboid_w')
    cuboid_h=st.number_input('Height h',0.0,key='cuboid_h')

col3dacb,col3dbcb=st.columns(2)

with col3dacb:
    st.metric('TSA',tsa_cuboid(cuboid_l,cuboid_w,cuboid_h))

with col3dbcb:
    st.metric('Volume',volume_cuboid(cuboid_l,cuboid_w,cuboid_h))

st.divider()

st.subheader('Sphere')

col3sp,col4sp=st.columns([1,3])

with col3sp:
    sphere_r=st.number_input('radius r',0.0,key='sphere_r')

col3dasp,col3dbsp=st.columns(2)

with col3dasp:
    st.metric('TSA',tsa_sphere(sphere_r))

with col3dbsp:
    st.metric('Volume',volume_sphere(sphere_r))
