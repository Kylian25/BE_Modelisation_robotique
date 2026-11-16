import numpy as np

ALPHA_I = [0, -np.pi/2, 0, np.pi/2, -np.pi/2, np.pi/2]
A_I = [0, 0, 0.400, 0, 0, 0]
R_I = [0.375, 0, 0.020, 0.450, 0, 0.070]
OFFSET_I = [0, -np.pi/2, np.pi/2, 0, 0, 0]


def mgd(q , i = 0 , j = 6):
    mat = np.eye(4)

    for i in range(i,j):
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

    return mat

def mgd_Xp(mat):
    return mat[0:3, 3]

def mgd_Xr(mat):
    return mat[0:3, 0:3]

