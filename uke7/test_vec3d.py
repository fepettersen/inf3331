from vec3d import Vec3D
u = Vec3D(1,0,0)
v = Vec3D(0,1,0)

print 'str(u): ',str(u)
print 'repr(v): ',repr(v)
print 'u[1] = ',u[1]
v[2] = 2.5
print 'set v[2] = :',v[2]
d = u+v
print 'u+v = ',d
e = u-v
print 'u-v = ',e
f = u**v
print 'cross product u x v = ',f
print 'scalar product u*v = ',u*v

print 'u.len() = ',u.len()
