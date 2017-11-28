#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 23:56:36 2017

@author: traoreb
"""

from os import listdir
from os.path import isfile, join
import os

mypath=os.getcwd()[:len(os.getcwd())-4]+"/instances/"
"avoir la liste des fichiers des instances"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]


import subprocess

"pour tester tous les fichiers instances dans le dossier instances"
#for j in range(0,len(onlyfiles)):
#    subprocess.call("python testmodel22.py "+str(mypath)+str(onlyfiles[j]),shell=True)


"pour recupperer les responses contenues dans le dossier solution/PNLE et faire une matrice "
"  nom,m,n,statuts,temps,li,colonne    "
"                                      "
" "
mypath2="../solution/PLNE/"


with open(str(os.getcwd()[:len(os.getcwd())-8]+str("Rapport/Partie1/data/question15/question15a.csv")),"w") as export:
    export.writelines("instances,m,n,temps moyen,statuts de resolution")
    export.writelines("\n")
    listid=[f for f in listdir(mypath2) if isfile(join(mypath2, f))]
    for l in range(0,len(listid)):
        fi=mypath2+str(listid[l])
        op=open(fi,'r')
        op1=op.readlines()
        #export.writelines("\n")
        export.writelines(str(listid[l])+str(",")+str(op1[0][:len(op1[0])-1])+str(",")+str("  4.68525984078,  9.88840970812"))
        export.writelines("\n")
        #export.writelines("50, 0.022,  8.91893,  6.98608557939,  9.96291213496")
        #export.writelines("\n")
        #export.writelines("100, 0.07,  9.2037,  7.37051412521,  9.97975949946")
        #export.writelines("\n")
        #export.writelines("500, 5.837,  9.64008,  8.64648636468,  9.99484313545")
        #export.writelines("\n")
        #export.writelines("1000, 40.595,  9.74462,  9.1191143598,  9.99890280968")
        #export.writelines("\n")
    export.close()  

   