# -*- coding: utf-8 -*-
"""
Created on Sun Nov  11 12:29:35 2026

@author: Emmanuel Tetouom
"""
import numpy as np
def calculpn(Tij):
    Pn={}
    T0_N={}
    Zn={}
    for i  in range(len(Tij)):
        T0_N[i+1]=np.eye(4)
        for j in range(i+1):
            T0_N[i+1]=T0_N[i+1]@Tij[j]

    for i in range(len(Tij)):
        
        Pn["P0"+str(i+1)]=T0_N[i+1][:3,3]
        Zn["z"+str(i+1)]=T0_N[i+1][:3,2]
    
    return Pn,Zn


def Jacobienne(Tij):
    Pn,zn=calculpn(Tij)
    J=np.zeros((6,6))

    for i in range(len(zn)):
        J[:3,i]=np.cross(zn["z"+str(i+1)],Pn["P06"]-Pn["P0"+str(i+1)])
        J[3:,i]=zn["z"+str(i+1)] 
    return J


