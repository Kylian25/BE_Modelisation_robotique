import numpy as np

#Variables de situation
theta_i = [0,0,0,0,0,0]
q_i = theta_i

#Constantes
sigma_i = [0,0,0,0,0,0]
alpha_i = [0,-np.pi/2,0,np.pi/2,-np.pi/2,np.pi]
a_i = [0,0,0,0,0,0]
r_i = [335,0,400,450,0,70]

parametres = {
    'sigma_i' : sigma_i,
    'alpha_i' : alpha_i,
    'a_i' : a_i,
    'r_i' : r_i,
    'theta_i' : theta_i,
    'q_i' : q_i,
}

def mgd(parametres,q_start=None,q_end=None):
    if not q_start:
        q_start = 0
    if not q_end:
        q_end = len(parametres['q_i'])

    mat = np.array(([1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]))

    return mat

print(mgd(parametres))
