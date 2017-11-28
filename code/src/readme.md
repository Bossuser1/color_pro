#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 18:53:49 2017

@author: traoreb
"""

#pour le solveur guroby (Modele.py)
#pour la resolution programmation dynamique (dynamiquesolv.py)
#proddynamique.py
#http://127.0.0.1:8004/test/lecturefichierexterne/

toto :

Memento (servira de support pour mon rapport pdf et me permettra de gagner 1 jour de Taf)
========Je me parle seul=====
j est la colonne (j=0,....,m-1)

l est le nombre de sequence (1,.....k)
mais l peux etre egale a 0 alors pas de sequence sur la ligne li en question.

(Je fais mon raisonement d'abord sur les lignes li fixés pas assez fort pour prendre en compte les deux parametres à la fois)


Q1: #Case l

si on calcule tous les T(j,l) bien evidement pour une ligne i fixée il suffit de voir si T(m-1,k) est a vrai ou Faux .

Ps se rappeler que notre variable T(j,l) est boolenne (True ou False) 

#T(j,l) (True ou False)

#case ou l=0 (pas de bloc)

en me basant sur le cours de mon Chretienne il est convenanble de mettre T(j,l) a True

#T(j,l)=True if l=0

#comme dans le cours du 24/11 l'un des propos du prof etant la sauvegarde du calcul precedant des T(j,l)
#et en citant en exemple la suite de fibonacci bon ("un clin d'oeil au concours d'entrée a l'ecole de stat, le monde était plus simple et je ne devais pas composer avec beaucoup d'equation comme ou dormir la nuit "le nombre d'or)

#il avait dit que la complexite ne serait pas au niveau du temps de calcul mais au niveau de la taille des elements effectivement 
#quand je commence a penser au nombre de ligne et a chaque T[j,l] a stocker ,bon deja je travail sur pour PC et après je me connecte
#sur la console PPTI ou lundi matin je vais a la fac pour les grandes instances 



avec python soit 

on se pose la question de savoir si on peux partitionner 


def partition(s,B):
    s1=[0]
    for el in s:
        s1.append(el)
    s=s1    
    n=len(s)
    b=np.zeros(shape=(n,B+1))
    b[0][0]=1
    for k in range(1,B+1):
        b[0][k]=0

    for i in range(1,n):
        for k in range(0,B+1):
            if (k-int(s[i])>-1):
                b[i][k]=max(b[i-1][k],b[i-1][k-s[i]])
            else:
                b[i][k]=max(b[i-1][k],b[0][k])    
    return b

data=partition([10,5,6,4,6],12)
data[5][12] retourne vrai



je decide d'adapter le code à mon probleme

faire beaucoup attention car a l'UPMC on ne dis pas tout

ici m-1 intrige deja, je pense que ca va marche car dans le code du prof j'ai utiliser B+1

#voila qu'ils ont commencer a me melanger avec des j et des l 

"nbre ici est m-1"
"l=1,....,k, ici on donne un li comme s"
def partition_Etape1(s,nbre):
    s1=[0]
    for el in s:
        s1.append(el)
    s=s1        
    T=np.zeros(shape=(s,nbre+1))        
    n=len(s)
    T[0][0]=1
    'k correspond a mon l (mes bloks considerés'
    ''
    for k in range(1,nbre+1):
        T[0][k]=0 #question 1 #ici k correspond a mon l
    for i in range(1,n): 
        for k in range(0,nbre+1):
            if (k-int(s[i])>-1):
                T[i][k]=max(T[i-1][k],T[i-1][k-s[i]]) #question 2c
            else:
                T[i][k]=max(T[i-1][k],T[0][k]) #question 2a 
    return T


"en appliquans ceux ci on regard"
ligneli,k,m=funtionli(g,4)
nbre=m-1
s=ligneli
data1=partition_Etape1(s,nbre)


sur l'instance 12 la ligne 23
g=learnfile("12.txt","/home/traoreb/Bureau/MOGPLPROJET/code/instances/")

ligneli,k,m=funtionli(g,23)
nbre=m-1
s=ligneli
data1=partition_Etape1(s,nbre)

on a [2 8 12] si on considere toute les sequences alors pour voir si il est possible de colorier ,
je regarder sum(sequence),nombre de sequence.


on constate que data1[len(ligneli),sum(ligneli)] nous donne vrai
T()

#Pseudo code

Algorithme 1 Algorithme de résolution partielle
1: procédure Coloration(A)
2: LignesAVoir ← {0, . . . , N − 1}
3: ColonnesAVoir ← {0, . . . , M − 1}
4: tant que LignesAVoir != ∅ ou ColonnesAVoir != ∅ faire
5:      pour i dans LignesAVoir faire
6:          Tester par programmation dynamique les cases non coloriées de la ligne A i
7:          Nouveaux ← {j : j est une nouvelle case coloriée}
8:          ColonnesAVoir ← ColonnesAVoir ∪ Nouveaux
9:          LignesAVoir ← LignesAVoir − {i}
10:     fin pour
11:     pour j dans ColonnesAVoir faire
12:         Tester par programmation dynamique les cases non coloriées de la colonne A j
13:         Nouveaux ← {i : i est une nouvelle case coloriée}
14:         LignesAVoir ← LignesAVoir ∪ Nouveaux
15:         ColonnesAVoir ← ColonnesAVoir − {j}
16:     fin pour
17: fin tant que
18: fin procédure


#
#sa=[0,4,10,1,5,12,7,9,9,10,7]
#
#
#import numpy as np
#B=36
#
#ba=np.zeros(shape=(11,B+1))
#
#ba=ba+1000
#
#ba[0][0]=1
#
#def fun(k,sa,i):
#    if k-sa[i]<0:
#       res=1
#    else:
#       res=k-sa[i]
#    return res
#
#for k in range(1,B+1):
#    ba[0][k]=0
#
#for i in range(1,11):
#    print i
#    for k in range(0,B+1):
#         if ba[i-1,][k]==1:
#             ba[i][k]=1#,b(i-1,k-sa[i])  
#         elif ba[i-1][fun(k,sa,i)]==1:
#             ba[i][k]=1
#         else:
#             ba[i][k]=0
#             #,b(i-1,k-sa[i])
#
#            #print b(i,k)