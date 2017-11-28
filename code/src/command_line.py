#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 17:54:09 2017

@author: traoreb
"""

"essayer de lire un fichier de configuration instance quelqu'onque et retourne les"
"N , M et le bloc "

import sys
import os
import numpy as np
file_path = os.path.dirname(os.path.realpath(__file__))

def learnfile(argv,current_directory):
    fichier1=open(current_directory+argv,'r')
    A=fichier1.readlines()
    fichier1.close()
    line=[]
    colonne=[]
    pop=None
    for ki in range(len(A)):
        if ki==0:
            pop='row'
        if str(A[ki])=='#\n':
            pop='col'
        if pop=='col':
            colonne.append(A[ki].split("\n")[0])
        elif pop=='row':
            line.append(A[ki].split("\n")[0])
    colonne=colonne[1:]
    line=line
    #Nous considérons une grille de N lignes numérotées de 0 à N − 1#
    #M colonnes numérotées de 0 à M − 1#
    M=len(colonne)
    N=len(line)
    pop=None

    "decouper la donnee en structure "
    "  {(-1,-1),value,label}{(-1,0),value,label},{(-1,1),value,label}"
    "{(0,-1),value,label},{(0,0),value,label}"
    ""
    ""
    ""
    "{(-1,N-1),value,label}{(0,1),value,label}"
    ""
    #{position i,position j},value (1 pour noir,0 pour blanc) mais initialement tous a zeros,label important pour les cellules -1 pour le texte   
    structure={}
    label=None
    for i in range(N+1): #ligne
        label=''
        for j in range(M+1):#colonne
            try:
                if i-1==-1:
                    label=colonne[j-1]
            except:
                label=''
                pass
            try:
                if j-1==-1:
                    label=line[i-1]
            except:
                label=''
                pass
            if (i-1>=0 and j-1>=0) or (i-1==-1 and j-1==-1):
                label=''
            structure[str(i-1)+str(",")+str(j-1)]={'label':label,'value':0}
    data={'filename':argv,'M':M,'N':N,'colonne':colonne,'line':line,'structure':structure}
    return data



if __name__ =="__main__":
   if len(sys.argv[1].split("instances/"))>1:
   	filenames=sys.argv[1].split("instances/")
   	filename=filenames[1]#"16.txt"
   	director=filenames[0]+'instances/'
   else:
   	filenames=sys.argv[1].split("newfile/")
   	filename=filenames[1]#"16.txt"
   	director=filenames[0]+'newfile/'
   print learnfile(filename,director)
#/home/traoreb/Bureau/MOGPL PROJET/code/instances/1.txt
