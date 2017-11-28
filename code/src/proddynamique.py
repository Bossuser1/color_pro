#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 15:59:18 2017

@author: traoreb
"""

import numpy as np
from command_line import learnfile

import pandas


"====================================================================="
"programmation de l'algorithme de la Q4"
"====================================================================="

'==simple nettoyage transformation de string in int for sequence si'
def funtionli(g,i,opt1='line',opt2='M'):
    sequence=g[opt1][i].split(' ')
    tmpsequence=[]
    try:
        for i in sequence:
            tmpsequence.append(int(i))
        sequence=tmpsequence
    except:
        sequence=[]
    m=g[opt2]
    return sequence,len(sequence),m


"===================soit un dictionnaire pour stocker les elements calculer ========="

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

#data=partition([10,5,6,4,6],12)

#===les tailles de B en colonne ===
#===les tailles les objects consideres en lignes==
#===on se rend compte que b[5,12]=== (b[nbresobjects,Taillessouhaiter])
#print data[5][6]
#print data[5][4]
#faux car pas de sequences de tailles 3
#"==========adaptation===================="
"nbre ici est m-1"
"l=1,....,k, ici on donne un li comme s"
def partition_Etape1(s,nbre):
    s1=[0]
    for el in range(0,len(s)):
        if el==0:
            s1.append(int(s[el]))
        else:
            s1.append(int(s[el])+1)
    s=s1
    n=len(s)        
    T=np.zeros(shape=(n,nbre+1))        
    T[0][0]=1
    'k correspond a mon l (mes bloks considerés'
    ''
    for k in range(1,nbre+1):
        T[0][k]=0 #question 1 #ici k correspond a mon l
    for i in range(1,n): 
        for k in range(0,nbre+1):
            #if (i==1):
                if (k-int(s[i])>-1):
                    T[i][k]=max(T[i-1][k],T[i-1][k-int(s[i])]) #question 2c
                elif(k-int(s[i])==-1):
                    T[i][k]=1
                #
                #    if (i==n-1):
                #        T[i][k]=1
                #elif(k-int(s[i])<-1):
                #    T[i][k]=None    
                    #max(T[i-1][k],T[i-1][k-int(s[i])])    
                #else:
                #    T[i][k]=None#max(T[i-1][k],T[0][k]) #question 2a
            #else:
            #    if (k-int(s[i])>-1):
            #        T[i][k]=max(T[i-1][k-1],T[i-1][k-int(s[i])]) #question 2c
            #    else:
            #        T[i][k]=max(T[i-1][k-1],T[0][k-1]) #question 2a
    #complete
    #for i in range(1,n):
    #for k in range(0,nbre):
    #        if T[n,k]==1:
    row_labels = range(0,n)
    column_labels = range(0,nbre+1)   
    df = pandas.DataFrame(T, columns=column_labels, index=row_labels)
    return df
"application"
"imaginer un element qui remontre pour remplir les cases non remplir"

#Q2 Pour chacun des cas de base 1, 2a et 2b, indiquez si T (j, `) prend la valeur vrai ou faux,
#éventuellement sous condition.
#lorsque j=sl-1 vrai lorque que i=n
#pareil pour j<sl-1  alors on regarde les elements precedents for j 

#i in 
#    b in range(j+sl[i-1],j+sl[i])
        

#print data1[len(ligneli),sum(ligneli)]

"ecriture d'une fonction qui lit une ligne/colonne avec les 3 marques"
" coloriées en blanc, colories en noirs et non explorer"
"PS etant données la logique , il est souhaitable que les auqucun non explorer soit"
"avant ou au milieu d'une sequence de cases coloriés "

#les marqueurs 0 pour blanc, 1 pour noir et -1 pour non explorer"

def lecturepreexplorer(ligne):
    "exemple ligne=[1,1,1,1,0,1,0,0,0,-1,-1,-1]"
    "resultat {'taillesoussequence': [4, 1], 'ligne_colonne': [1, 1, 1, 1, 0, 1, 0, 0, 0, -1, -1, -1], 'positionfinsousequence': [3, 5], 'soussequence': [0, 1, 2, 3, 5]}"
    seque_o=[]
    j_finale=0
    for j in range(0,len(ligne)):
        if ligne[j]==1:
            seque_o.append(j)
    for i in range(0,len(ligne)):
        if ligne[i]==-1:
            j_finale=i
            break            

    nbre_seque_o=1
    seque_ofin=[]
    seque_taille=[]
    cpt=1
    for k in range(0,len(seque_o)-1):
        #print str(int(seque_o[k])-int(seque_o[k+1]))
        if (int(seque_o[k])-int(seque_o[k+1])) not in [-1,1]:
            nbre_seque_o=nbre_seque_o+1        
            seque_ofin.append(int(seque_o[k]))
            seque_taille.append(cpt)
            cpt=1
        else:
            cpt=cpt+1        
    "servira a preremplir mes T(j,l)"
    seque_ofin.append(int(seque_o[len(seque_o)-1]))    
    seque_taille.append(int(seque_ofin[len(seque_ofin)-1])-int(seque_ofin[len(seque_ofin)-2])-1)
    datainfor={}
    datainfor['ligne_colonne']=ligne
    datainfor['soussequence']=seque_o
    datainfor['positionfinsousequence']=seque_ofin
    datainfor['taillesoussequence']=seque_taille
    datainfor['dernierepositionnonmarque']=j_finale     
    return datainfor 






def partition_Etape2(s,nbre):
    s1=[0]
    for el in range(0,len(s)):
        if el==0:
            s1.append(int(s[el]))
        else:
            s1.append(int(s[el])+1)
    s=s1
    n=len(s)        
    T=np.zeros(shape=(n,nbre+1))        
    T[0][0]=1
    'k correspond a mon l (mes bloks considerés'
    ''
    for k in range(1,nbre+1):
        T[0][k]=0 #question 1 #ici k correspond a mon l
    for i in range(1,n): 
        for k in range(0,nbre+1):
            #if (i==1):
                if (k-int(s[i])>-1):
                    T[i][k]=max(T[i-1][k],T[i-1][k-int(s[i])]) #question 2c
                elif(k-int(s[i])==-1):
                    T[i][k]=1
                #
                #    if (i==n-1):
                #        T[i][k]=1
                #elif(k-int(s[i])<-1):
                #    T[i][k]=None    
                    #max(T[i-1][k],T[i-1][k-int(s[i])])    
                #else:
                #    T[i][k]=None#max(T[i-1][k],T[0][k]) #question 2a
            #else:
            #    if (k-int(s[i])>-1):
            #        T[i][k]=max(T[i-1][k-1],T[i-1][k-int(s[i])]) #question 2c
            #    else:
            #        T[i][k]=max(T[i-1][k-1],T[0][k-1]) #question 2a
    #complete
    #for i in range(1,n):
    #for k in range(0,nbre):
    #        if T[n,k]==1:
    row_labels = range(0,n)
    column_labels = range(0,nbre+1)   
    df = pandas.DataFrame(T, columns=column_labels, index=row_labels)
    return df



#print lecturepreexplorer(ligne)



#Tjl=np.zeros(shape=(k+1,m+2))
#Tjl=Tjl+10000
"en ligne le l (les sequences considerés)"
"en colonne les j considerées"
"on initialise une matrice avec des valeurs infini"

"initilasation des Tjl a pour 0,0 on n'as varie"
#Tjl[0][0]=1
#for k in range(1,m-1):
#    Tjl[0][k]=1


#==================Algorithme de Propagation=======================#
    
"A est une grille à colorié"
"soit une matrice ou dictionnaire mais opter pour un dictionnaire"
#ligne=[1,1,0,0,0,0,-1,-1,-1,-1,-1]
ligne=[1,1,0,0,0,0,1,1,1,-1,-1]
dat=lecturepreexplorer(ligne)

sequenceli=[2,3,4]#gerer les retraits
sequedeja=[2,3]
d=list(set(sequenceli)-set(sequedeja))
if len(d)>0:
   n=len(d)+1
else:
    n=1
nbre=len(ligne)
"sous tableau"
"[T[l-1]"
"T[l]]"
T=np.zeros(shape=(n,nbre+1))   
for j in range(dat['dernierepositionnonmarque'],nbre+1):
    T[0][j]=None    
for j in range(0,dat['dernierepositionnonmarque']):
    T[0][j]=ligne[j]         
d1=[0]
for kv in d:
    d1.append(kv)
d=d1
cp=-(int(dat['dernierepositionnonmarque'])-int(dat['soussequence'][-1]))+1
if cp>-1:
    cp=0
    
for i in range(1,n): 
       for k in range(dat['dernierepositionnonmarque'],nbre):
                if (k-int(d[i])>-1):
                    if np.isnan(T[i-1][k-int(d[i])+cp]) and np.isnan(T[i-1][k]):
                        T[i][k]=10000
                    elif np.isnan(T[i-1][k-int(d[i])+cp]):
                        T[i][k]=T[i-1][k]
                    elif np.isnan(T[i-1][k]):
                        T[i][k]=T[i-1][k-int(d[i])+cp]
                    else:
                        T[i][k]=T[i][k]=max(T[i-1][k],T[i-1][k-int(d[i])+cp])
                else:
                    print k
#def coloration(A):    
if __name__ =="__main__":
    g=learnfile("1.txt","/home/traoreb/Bureau/MOGPLPROJET/code/instances/")
    ligneli,k,m=funtionli(g,0)
    #m=15
    ligneli=[2]
    data1=partition_Etape1(ligneli,m-1)

