import math

def distance(a,b):
    return length(diff_vector(a, b))

def unitvector(a):
    l = length(a)
    a1, a2 = a
    if l == 0:
        return 0,0

    return a1/l, a2/l

def length(a):
    a1, a2 = a
    s = a1**2 + a2**2
    return math.sqrt(s)

def add(a, b):
    a1, a2 = a
    b1, b2 = b
    out = a1+b1, a2+b2
    return out

def diff_vector(a, b):
    a1, a2 = a
    b1, b2 = b
    out = a1-b1, a2-b2
    return out

def diff_unitvector(a, b):
    return unitvector(diff_vector(a,b))

def scale(a, scalefactor):
    a1, a2 = a
    return a1*scalefactor, a2*scalefactor

def angle_vect(rad):
    x = math.cos(rad)
    y = math.sin(rad)
    return x,y

def to_int(a):
    x, y = a
    return int(x), int(y)