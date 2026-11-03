import numpy as np

ALPHA_I = [0, -np.pi/2, 0, np.pi/2, -np.pi/2, np.pi/2]
A_I = [0, 0, 400, 0, 0, 0]
R_I = [375, 0, 20, 450, 0, 70]
OFFSET_I = [0, -np.pi/2, np.pi/2, 0, 0, 0]
T_OUTIL = np.array([
    [ 0,  0, -1,  0],
    [ 0,  1,  0,  0],
    [ 1,  0,  0,  0],
    [ 0,  0,  0,  1]
])

def mgd(q):
    mat = np.eye(4)

    for i in range(6):
        th = q[i] + OFFSET_I[i]
        r = R_I[i]
        a = A_I[i]
        al = ALPHA_I[i]

        cos_th = np.cos(th)
        sin_th = np.sin(th)
        cos_al = np.cos(al)
        sin_al = np.sin(al)

        mat_i = np.array((
            [cos_th, -sin_th, 0, a],
            [cos_al*sin_th, cos_al*cos_th, -sin_al, -r*sin_al],
            [sin_al*sin_th, sin_al*cos_th, cos_al, r*cos_al],
            [0, 0, 0, 1]))

        mat = np.dot(mat, mat_i)

    mat = np.dot(mat, T_OUTIL)
    
    return mat

def mgd_Xp(mat):
    return mat[0:3, 3]

def mgd_Xr(mat):
    return mat[0:3, 0:3]

q_test = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
T = mgd(q_test)
Xp = mgd_Xp(T)
Xr = mgd_Xr(T)

print(Xp)
print(Xr)